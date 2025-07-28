There is an RSS feed that exists at https://www.reddit.com/r/BlackWolfFeed.rss. Each entry in the RSS feed looks like this:

```xml
	<entry>
		<author>
			<name>/u/Long-Anywhere156</name>
			<uri>https://www.reddit.com/user/Long-Anywhere156</uri>
		</author>
		<category term="BlackWolfFeed" label="r/BlackWolfFeed"/>
		<content type="html">&amp;#32; submitted by &amp;#32; &lt;a href=&quot;https://www.reddit.com/user/Long-Anywhere156&quot;&gt; /u/Long-Anywhere156 &lt;/a&gt; &lt;br/&gt; &lt;span&gt;&lt;a href=&quot;https://soundgasm.net/u/ClassWarAndPuppies/952-The-Sissy-Boy-Initiative-feat-Liv-Agar-Spencer-Barrows-071725&quot;&gt;[link]&lt;/a&gt;&lt;/span&gt; &amp;#32; &lt;span&gt;&lt;a href=&quot;https://www.reddit.com/r/BlackWolfFeed/comments/1m2w1l8/952_the_sissy_boy_initiative_feat_liv_agar/&quot;&gt;[comments]&lt;/a&gt;&lt;/span&gt;</content>
		<id>t3_1m2w1l8</id>
		<link href="https://www.reddit.com/r/BlackWolfFeed/comments/1m2w1l8/952_the_sissy_boy_initiative_feat_liv_agar/" />
		<updated>2025-07-18T07:35:42+00:00</updated>
		<published>2025-07-18T07:35:42+00:00</published>
		<title>952 · The Sissy Boy Initiative feat. Liv Agar &amp; Spencer Barrows [071725]</title>
	</entry>
```

The `[link]` formatted link typically links to a soundgasm.net page with the episode file I care about. That episode file can be found in a media element, here's the HTML of a sample page when viewed from source:

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>soundgasm.net</title>

        <link href='//fonts.googleapis.com/css?family=Ubuntu:400,500,700|Roboto' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="//static.soundgasm.net/css/site.css" />
        
        <link type="text/css" href="//static.soundgasm.net/css/jplayer.blue.monday.css" rel="stylesheet" />        
</head>

<body>
    <header>
        <a href="/" class="logo">Soundgasm.net Logo</a>
        <nav>
            <a href="https://soundgasm.net/">Home</a><a href="https://soundgasm.net/login">Login</a><a href="https://soundgasm.net/signup">Signup</a><a href="https://soundgasm.net/contact">Contact</a>        </nav>
    </header>
<div style="margin:10px 0">
    <a href="https://soundgasm.net/u/ClassWarAndPuppies">ClassWarAndPuppies</a></div>
<div id="jquery_jplayer_1" class="jp-jplayer"></div>
  <div id="jp_container_1" class="jp-audio">
    <div class="jp-type-single">
      <div class="jp-gui jp-interface">
        <div class="jp-controls">
          <button class="jp-play" role="button" tabindex="1">play</button>
          <button class="jp-stop" role="button" tabindex="1">stop</button>
        </div>
        <div class="jp-progress">
          <div class="jp-seek-bar">
            <div class="jp-play-bar"></div>
          </div>
        </div>
        <div class="jp-volume-controls">
          <button class="jp-mute" role="button" tabindex="1" title="mute">mute</button>
          <button class="jp-unmute" role="button" tabindex="1" title="unmute">unmute</button>
          <button class="jp-volume-max" role="button" tabindex="1" title="max volume">max volume</button>
          <div class="jp-volume-bar">
            <div class="jp-volume-bar-value"></div>
          </div>
        </div>
        <div class="jp-time-holder">
          <div class="jp-current-time"></div>
          <div class="jp-duration"></div>
          <div class="jp-toggles">
            <button class="jp-repeat" role="button" tabindex="1" title="repeat">repeat</button>
          </div>
        </div>
      </div>
      <div class="jp-details">
        <div class="jp-title" aria-label="title">954 · The Peoples’ Crisis feat. Seeking Derangements [07.24.25]</div>
      </div>
      <div class="jp-description">
          <p style="white-space: pre-wrap;">Will on vacation; Seeking Derangements guest hosting; Felix’s internet connection fraying; Sanity rapidly depleting…Episode Report: NORMAL.

ONE WEEK LEFT to pre-order YEAR ZERO: A Chapo Trap House Comic Anthology at badegg.co/products/year-zero-1

If you’re in LA, come to the anti-ICE benefit at Grandmaster Recorders this Friday 7/25: https://www.instagram.com/littlesecret_la/p/DMJKf0Rh7sI/

https://thecomedybureau.com/show/little-secret-anti-ice-benefit-in-la/</p>
      </div>
      <div class="jp-no-solution">
        <span>Update Required</span>
        To play the media you will need to either update your browser to a recent version or update your <a href="http://get.adobe.com/flashplayer/" target="_blank">Flash plugin</a>.
      </div>
    </div>
  </div>

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
<script type="text/javascript" src="//static.soundgasm.net/js/jquery.jplayer.2.9.2.min.js"></script><script type="text/javascript">
    $(document).ready(function(){
      $("#jquery_jplayer_1").jPlayer({
        ready: function () {
          $(this).jPlayer("setMedia", {
            m4a: "https://media.soundgasm.net/sounds/62371ba7654e4525e537b3f14b903e8318007d53.m4a"
          });
        },
        swfPath: "/swf",
        supplied: "m4a",
        useStateClassSkin: true,
        autoBlur: false,
        smoothPlayBar: true,
        keyEnabled: true,
        remainingDuration: true,
        toggleDuration: true
      });
    });
  </script>
</body>

</html>
```

(Note that the `m4a` attribute in the script at the bottom is the link we care about)

The rendered HTML in a webpage looks like this:

```html
<div id="jquery_jplayer_1" class="jp-jplayer" style="width: 0px; height: 0px;"><img id="jp_poster_0" style="width: 0px; height: 0px; display: none;"><audio id="jp_audio_0" preload="metadata" src="https://media.soundgasm.net/sounds/62371ba7654e4525e537b3f14b903e8318007d53.m4a"></audio></div>
```

A more standard RSS feed for a podcast might have entries that look like this:

```xml
<item>
      <guid isPermaLink="false">tag:soundcloud,2010:tracks/2130109572</guid>
      <title>951 - My Boys And In Some Cases Gals feat. Alex Nichols (7/14/25)</title>
      <pubDate>Tue, 15 Jul 2025 06:48:02 +0000</pubDate>
      <link>https://soundcloud.com/chapo-trap-house/951-my-boys-and-in-some-cases-gals-feat-alex-nichols-71425</link>
      <itunes:duration>01:07:56</itunes:duration>
      <itunes:author>Chapo Trap House</itunes:author>
      <itunes:explicit>yes</itunes:explicit>
      <itunes:summary>Alex back on the show today to look at the continuing fallout of Trump’s attempts to wash his hands of Epstein. From the baffled &amp; betrayed Trump-curious internet trend-seekers, to the dyed-in-the-wool loyalists, the admin seems to have picked the absolute worst way to disarm this bomb. Plus: Greg Abbott makes a why-even-bother play to cover up Musk’s bribery, and Biden gives a why-even-bother explanation for his diminished capacity pardons.

Pre-Order YEAR ZERO: A Chapo Trap House Comic Anthology at badegg.co/products/year-zero-1</itunes:summary>
      <itunes:subtitle>Alex back on the show today to look at the contin…</itunes:subtitle>
      <description>Alex back on the show today to look at the continuing fallout of Trump’s attempts to wash his hands of Epstein. From the baffled &amp; betrayed Trump-curious internet trend-seekers, to the dyed-in-the-wool loyalists, the admin seems to have picked the absolute worst way to disarm this bomb. Plus: Greg Abbott makes a why-even-bother play to cover up Musk’s bribery, and Biden gives a why-even-bother explanation for his diminished capacity pardons.

Pre-Order YEAR ZERO: A Chapo Trap House Comic Anthology at badegg.co/products/year-zero-1</description>
      <enclosure type="audio/mpeg" url="https://dts.podtrac.com/redirect.mp3/feeds.soundcloud.com/stream/2130109572-chapo-trap-house-951-my-boys-and-in-some-cases-gals-feat-alex-nichols-71425.mp3" length="65227597"/>
      <itunes:image href="https://i1.sndcdn.com/artworks-qiEyLv8tDP2M5b28-8kx7Bg-t3000x3000.png"/>
    </item>
```

or this:

```xml
<item>
<title>
397 - Love Out of Bounds: Rebound of Love: A Ref’s Story: Whistle of Love
</title>
<link>
https://www.patreon.com/posts/397-love-out-of-134859733
</link>
<itunes:image href="https://c10.patreonusercontent.com/4/patreon-media/p/campaign/1170927/415e52f2ef2e4ee0a89d386dd2f4874f/eyJkIjo3MiwiaCI6MzAwMCwic3RyaXBfYWxwaGEiOjEsInciOjMwMDAsIndlYnAiOjB9/1.png?token-hash=fajAaCjqIl4Kjj8KURzEsgKcdfT3qw9OeB0cXXPngBc%3D"/>
<description>
<p>Ref Nate is the #1 draft pick in the NBA Ref Draft. But when he falls in love with a player named Raz Hummler, will his personal feelings interfere with his ability to call the game fairly? For the first time in his life, this ref is going to take his shot. Lost scripted episode written in 2021.</p><p>With Nate Ruess, @tom_on_here, Charles Austin, Andrew Hudson, and Alex Branson</p>
</description>
<enclosure url="https://c10.patreonusercontent.com/4/patreon-media/p/post/134859733/c061452212ad4a08920415b3a3aa6d65/eyJhIjoxLCJpc19hdWRpbyI6MSwicCI6MX0%3D/1.mp3?token-hash=4YbFd_CToSDcnBbSHm4x_LsYXElrvTUmdMnrUBPId7A%3D&token-time=1754352000" length="167591360" type="audio/mpeg"/>
<guid isPermaLink="false">134859733</guid>
<pubDate>Thu, 24 Jul 2025 15:04:31 GMT</pubDate>
</item>

```


I want you to design a very simple python webapp which will, when `/feed.rss` is accessed, will do the following:
1. Read in the latest list of RSS feed entries from the provided reddit link
2. Scrape each `[link]` that is a `soundgasm` link for the related audio
3. Use the episode title and description from the original RSS feed, along with the link to the audio file from `soundgasm`, to produce a new RSS feed which represents the podcast with the actual audio files


Some constraints:
- We should use `uv` for any python management
- It should be dockerized
- It should be as simple as possible
