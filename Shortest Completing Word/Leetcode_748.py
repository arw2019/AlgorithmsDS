from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        lpCount = Counter(char for char in licensePlate.lower() if char.isalpha())
        
        ans = '-'*16
        for word in words:
            if len(word) < len(ans):
                if all(word.count(char)>=n for char, n in lpCount.items()):
                    ans = word
                    
        return ans
