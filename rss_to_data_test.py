import unittest
from feedparser.util import FeedParserDict

class ConvertRSSToDataTestCase(unittest.TestCase):

    def testPlayWithDictionaries(self):
        dictionary = {'title': 'this is a title'}
        self.assertEqual('this is a title', dictionary['title'])
        
        dictionary.update({'updated': 'updated item'})
        self.assertEqual('updated item', dictionary['updated'])

    def testCreateFeedParserDict(self):
        feed = FeedParserDict()
        list = [FeedParserDict()]
        list[0].update({'title': 'this is the title'})
        self.assertEqual(list[0]['title'],'this is the title')

        feed.entries = list
        self.assertEqual(feed.entries[0]['title'],'this is the title')

def testPlayWithFeedParserDictConstructor(self):
        feed = FeedParserDict(entries=[FeedParserDict()])
        self.assertEqual(feed.entries[0]['title'],'this is the title')

def xtestSemanticData(self):
        data = createOneEntry()

