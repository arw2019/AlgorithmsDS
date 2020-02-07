# dynamic program
# O(m*n) runtime

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cur = [True] + [False]*(m)
        print(cur)
        for j in range(1, n+1):
            pre = cur[0]
            cur[0] = cur[0] and (p[j-1] == '*')
            for i in range(1, m+1):
                if p[j-1] != '*':
                    pre, cur[i] = cur[i], pre and (s[i-1]==p[j-1] or p[j-1]=='?')
                else:
                    pre, cur[i] = cur[i], cur[i-1] or cur[i]
        return cur[m]

# finite-state machine solution

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        transfer = {}
        state = 0
        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1
        
        print(transfer)  

        accept = state
        state = {0}
        
        for char in s:
            state = {transfer.get((at, token)) for at in state for token in (char, '*', '?')}
        
        return accept in state
