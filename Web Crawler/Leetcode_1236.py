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

# top 0.7%
# cleaner code. Do dfs via a helper function embedded inside self.crawl
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getHostName(url: str) -> str:
            urlWithoutHttp = url[7:]
            hostName = urlWithoutHttp.split("/")[0]
            return "http://" + hostName
        def dfs(url: str, hostName: str, htmlParser: htmlParser, seen: set) -> None:
            if url not in seen and hostName == getHostName(url):
                seen.add(url)
                for link in htmlParser.getUrls(url):
                    dfs(link, hostName, htmlParser, seen)
        seen = set()
        dfs(startUrl, getHostName(startUrl), htmlParser, seen)
        return list(seen)

#top 5%
# DFS solution implemented by recursion on the self.crawl function
# class Solution:
#     def __init__(self):
#         self.seen = set()
#         self.hostname = None
#     def crawl(self, startUrl: str, htmlParser: 'HtmlParser', flag: bool = True) -> List[str]:
#         if not self.hostname:
#             self.hostname = startUrl.split('/')[2]
#         if startUrl.split('/')[2] != self.hostname or startUrl in self.seen:
#             return
#         self.seen.add(startUrl)
#         for url in htmlParser.getUrls(startUrl):
#             self.crawl(url, htmlParser, False)
#         if flag: return self.seen