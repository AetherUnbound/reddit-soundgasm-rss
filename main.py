import re
import time
import logging
from typing import List, Optional, Tuple
from datetime import datetime, timezone

import feedparser
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Response
from feedgen.feed import FeedGenerator

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RSS_SOURCE = "https://www.reddit.com/r/BlackWolfFeed.rss"
CACHE_DURATION = 3600  # 1 hour in seconds
PODCAST_IMAGE = "https://static-cdn.jtvnw.net/jtv_user_pictures/55a81036-85b5-426d-8a0b-4096f0d9b732-profile_image-300x300.jpg"

# Simple in-memory cache
_cache: Optional[Tuple[float, str]] = None


def extract_soundgasm_links(content: str) -> List[str]:
    """Extract soundgasm.net links from RSS entry content."""
    soup = BeautifulSoup(content, 'html.parser')
    soundgasm_links = []
    
    for link in soup.find_all('a', href=True):
        href = link['href']
        if 'soundgasm.net' in href and '/u/' in href:
            soundgasm_links.append(href)
    
    return soundgasm_links


def scrape_soundgasm_audio(url: str) -> Optional[str]:
    """Scrape soundgasm page to extract m4a audio URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Look for the m4a URL in the JavaScript
        match = re.search(r'm4a:\s*"([^"]+)"', response.text)
        if match:
            return match.group(1)
        
        # Alternative: look for audio tag in rendered content
        soup = BeautifulSoup(response.text, 'html.parser')
        audio_tag = soup.find('audio')
        if audio_tag and audio_tag.get('src'):
            return audio_tag['src']
            
        logger.warning(f"No audio URL found in {url}")
        return None
        
    except Exception as e:
        logger.error(f"Error scraping {url}: {e}")
        return None


def fetch_reddit_rss() -> List[dict]:
    """Fetch and parse the Reddit RSS feed."""
    try:
        response = requests.get(RSS_SOURCE, timeout=10)
        response.raise_for_status()
        
        feed = feedparser.parse(response.content)
        entries = []
        
        for entry in feed.entries:
            # Extract soundgasm links from the content
            soundgasm_links = extract_soundgasm_links(entry.get('content', [{}])[0].get('value', ''))
            
            if soundgasm_links:
                # Get audio URL from first soundgasm link
                audio_url = scrape_soundgasm_audio(soundgasm_links[0])
                if audio_url:
                    entries.append({
                        'title': entry.title,
                        'description': entry.get('summary', ''),
                        'link': entry.link,
                        'published': entry.get('published_parsed'),
                        'guid': entry.get('id', entry.link),
                        'audio_url': audio_url,
                        'soundgasm_url': soundgasm_links[0]
                    })
        
        return entries
        
    except Exception as e:
        logger.error(f"Error fetching RSS feed: {e}")
        return []


def generate_podcast_rss(entries: List[dict]) -> str:
    """Generate podcast RSS feed with audio enclosures."""
    fg = FeedGenerator()
    fg.title('BlackWolfFeed Audio')
    fg.description('Audio episodes from BlackWolfFeed subreddit')
    fg.link(href='https://www.reddit.com/r/BlackWolfFeed', rel='alternate')
    fg.id('https://www.reddit.com/r/BlackWolfFeed.rss')
    fg.language('en')
    fg.lastBuildDate(datetime.now(timezone.utc))
    
    # Add podcast-specific elements
    fg.load_extension('podcast')
    fg.podcast.itunes_category('Comedy')
    fg.podcast.itunes_explicit('yes')
    fg.podcast.itunes_complete('no')
    fg.podcast.itunes_type('episodic')
    fg.podcast.itunes_image(PODCAST_IMAGE)
    
    for entry in entries:
        fe = fg.add_entry()
        fe.title(entry['title'])
        fe.description(entry['description'])
        fe.link(href=entry['link'])
        fe.guid(entry['guid'])
        
        if entry['published']:
            fe.pubDate(datetime(*entry['published'][:6], tzinfo=timezone.utc))
        
        # Add audio enclosure and episode image
        fe.enclosure(entry['audio_url'], 0, 'audio/m4a')
        fe.load_extension('podcast')
        fe.podcast.itunes_image(PODCAST_IMAGE)
        
    return fg.rss_str(pretty=True).decode('utf-8')


@app.get("/feed.rss")
async def get_rss_feed():
    """Main endpoint that returns the converted RSS feed."""
    global _cache
    current_time = time.time()
    
    # Check if we have valid cached content
    if _cache and (current_time - _cache[0]) < CACHE_DURATION:
        logger.info("Serving cached RSS feed")
        return Response(content=_cache[1], media_type="application/rss+xml")
    
    logger.info("Fetching fresh RSS feed...")
    entries = fetch_reddit_rss()
    
    if not entries:
        logger.warning("No entries found")
        error_content = "<?xml version='1.0' encoding='UTF-8'?><rss version='2.0'><channel><title>Error</title><description>No entries found</description></channel></rss>"
        return Response(content=error_content, media_type="application/rss+xml")
    
    rss_content = generate_podcast_rss(entries)
    logger.info(f"Generated RSS feed with {len(entries)} entries")
    
    # Cache the generated content
    _cache = (current_time, rss_content)
    
    return Response(content=rss_content, media_type="application/rss+xml")


@app.get("/")
async def root():
    """Root endpoint with basic info."""
    return {"message": "Reddit Soundgasm RSS Converter", "feed_url": "/feed.rss"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)