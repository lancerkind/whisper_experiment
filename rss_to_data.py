import feedparser
import ssl

def retrieve_rss(url):
    """
    Returns a Request object upon loading a RSS feed from the URL.
    :param url: url to an RSS feed.
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    return feedparser.parse(url)

#def write_data()
url = "https://soundnotes.leadingagile.com/feed.xml"
print(retrieve_rss(url))
