class Solution:
    def countLetters(self, S: str) -> int:
        n = len(S)
        dp = [1] * n
        tot, prev = 1, 1
        for i in range(n-2, -1, -1):
            if S[i]==S[i+1]: 
                prev +=1
            else:
                prev=1
            tot += prev
        return tot
