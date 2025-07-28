# Reddit Soundgasm RSS Converter

A simple Python web application that converts Reddit RSS feeds to proper podcast RSS feeds with direct audio links.

## Overview

This application:
1. Fetches RSS entries from https://www.reddit.com/r/BlackWolfFeed.rss
2. Extracts soundgasm.net links from each entry
3. Scrapes each soundgasm page to get the actual m4a audio file URLs
4. Generates a properly formatted podcast RSS feed with audio enclosures

## Usage

### Local Development

```bash
# Install dependencies
uv sync

# Run the application
uv run python main.py
```

The application will be available at http://localhost:8000

- Main RSS feed: `http://localhost:8000/feed.rss`
- Health check: `http://localhost:8000/`

### Using Just (Recommended)

```bash
# Build the image
just build

# Start the application
just up

# Stop the application
just down

# Run locally for development
just dev

# Install dependencies
just install

# Test the RSS endpoint
just test
```

### Configuration

Create a `.env` file to customize the port:

```bash
# Copy the example file
cp .env.example .env

# Edit the port (default is 8000)
PORT=9000
```

### Docker

```bash
# Build the image
docker build -t reddit-soundgasm-rss .

# Run the container
docker run --rm -p 8000:8000 reddit-soundgasm-rss

# Or use Docker Compose
docker compose up
```

## Requirements

- Python 3.13+
- uv (for dependency management)
- Docker (for containerization)  
- Just (task runner, optional but recommended)

## Dependencies

- FastAPI - Web framework
- uvicorn - ASGI server
- feedparser - RSS parsing
- feedgen - RSS generation
- requests - HTTP client
- beautifulsoup4 - HTML parsing