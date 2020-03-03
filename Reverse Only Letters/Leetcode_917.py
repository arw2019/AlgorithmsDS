class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [char for char in S if char.isalpha()]
        if not letters: return S
        letters.reverse()
        res = []
        i=0
        for idx, char in enumerate(S):
            if char.isalpha():
                res+=letters[i]
                i+=1
            else:
                res+=char
        return ''.join(res)
