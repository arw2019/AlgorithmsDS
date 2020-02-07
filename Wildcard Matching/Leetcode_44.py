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
