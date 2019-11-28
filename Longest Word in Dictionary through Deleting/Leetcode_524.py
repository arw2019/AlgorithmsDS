class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        def isSubsequence(x: str, y: str) -> bool:
            """ check if y is a subsequence of x"""
            it = iter(y)
            return all(c in it for c in x)
        
        d.sort(key=len, reverse=True)
        
        res = []
        
        for word in d:
            if isSubsequence(word, s):
                if not res or len(word) == len(res[0]): res.append(word)
                else: break
        
        return sorted(res)[0] if res else ''