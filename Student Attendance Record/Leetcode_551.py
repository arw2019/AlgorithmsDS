class Solution:
    def checkRecord(self, s: str) -> bool:
        i, n = 0, len(s)
        while i < n:
            if s[i] == 'L':
                i+=1
                run = 1
                while i < n and s[i] == 'L': 
                    i += 1
                    run += 1
                if run > 2: 
                    return False
            else:
                i+=1
        return s.count('A') <= 1
