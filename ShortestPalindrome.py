class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        n = len(s)
        pos = -1
        B = 29
        MOD = 1000000007
        POW = 1
        hash1 = 0
        hash2 = 0
        i = 0
        while i < n:
            hash1 = (hash1 * B + ord(s[i])-ord('a')+1) % MOD
            hash2 = (hash2 + (ord(s[i]) - ord('a') +1)*POW ) % MOD
            if hash1 == hash2: pos = i
            i+=1
            POW = POW * B % MOD
        
        return "" + s[pos+1:n][::-1] + s