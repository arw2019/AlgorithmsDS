# top 0.7 %
# same algorithm implemented using python's in-built functions
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = list(map(len, s.replace('01', '0 1').replace('10','1 0').split(' ')))
        return sum([min(s[i], s[i-1]) for i in range(1, len(s))])
    
# O(N) time, constant space
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ones, zeros, ans = 0, 0, 0
        i = 0
        while i < len(s):
            ones = 0
            while i < len(s) and s[i] == '1':
                ones += 1
                i += 1
            ans += min(ones, zeros)
            zeros = 0
            while i < len(s) and s[i] == '0':
                zeros += 1
                i += 1
            ans += min(ones, zeros)
        return ans