import feedparser
import ssl

url = "https://soundnotes.leadingagile.com/feed.xml"
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
feed = feedparser.parse(url)

print(feed)
