# a different approach
# better time complexity (linear in number of palindromic substrings)
# time: 308ms (top 9%)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <=1: return s
        
        candidates  = [(i, i+1) for i in range(n)] + [(i, i+2) for i in range(0, n-1) if s[i] == s[i+1]]
        
        while True:
            # print(candidates)
            newCandidates = []
            for start, end in candidates:
                if start - 1 >= 0 and end < n and s[start-1]==s[end]:
                    newCandidates += [(start-1, end+1)]
            if not newCandidates:
                start, end = sorted(candidates, key=lambda x: x[1] - x[0], reverse=True)[0]
                return s[start:end]
            else:
                candidates.clear()
                candidates.extend(newCandidates)
             
                                   

## I thought there might be a further improvement if expand returns indicies rather than a slice. 
## Actually with that change the time is consistently worse by ~50ms

#248ms (top 92%)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]: return s
        result = ""
        for i in range(0, len(s)-1):
            result = max(result, self.expand(s, i, i+1), key=len)
            s2 = s[i:i+2]
            if s2==s2[::-1]: 
                result = max(result, self.expand(s, i, i+2), key=len)
        return result
    def expand(self, s: str, left: int, right: int) -> None:
        while left >= 0 and right <= len(s) and s[left]==s[right-1]:
            left -=1
            right +=1
        return s[left+1:right-1]

# 272ms (top 90%)
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) < 2 or s == s[::-1]: return s
#         result = ""
#         for i in range(0, len(s)-1):
#             s1, s2 = s[i:i+1], s[i:i+2]
#             if s1==s1[::-1] or s2 == s2[::-1]:
#                 result = max(result, self.expand(s, i, i+1), self.expand(s, i, i+2), key=len)
#         return result
#     def expand(self, s: str, left: int, right: int) -> None:
#         while left >= 0 and right <= len(s) and s[left]==s[right-1]:
#             left -=1
#             right +=1
#         return s[left+1:right-1]

# #920ms (top 85%)
# class Solution:
#     def __init__(self):
#         self.maxLen = 0
#         self.lo = None
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2: return s
#         for i in range(0, n-1):
#             self.extendPalindrome(s, i, i)
#             self.extendPalindrome(s, i, i+1)
#         return s[self.lo: self.lo+self.maxLen]
#     def extendPalindrome(self, s: str, j: int, k: int) -> None:
#         while j>=0 and k<len(s) and s[j]==s[k]:
#             j-=1
#             k+=1
#         if self.maxLen < k-j-1:
#             self.lo = j+1
#             self.maxLen = k-j-1
