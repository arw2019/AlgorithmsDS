# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def __init__(self):
        self.seen = set()
        self.hostname = None
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser', flag: bool = True) -> List[str]:
        if not self.hostname:
            self.hostname = startUrl.split('/')[2]
        if startUrl.split('/')[2] != self.hostname or startUrl in self.seen:
            return
        self.seen.add(startUrl)
        for url in htmlParser.getUrls(startUrl):
            self.crawl(url, htmlParser, False)
        if flag: return self.seen
