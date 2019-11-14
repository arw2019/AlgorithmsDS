class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split(' ')
        n = len(s)
        if len(pattern) != n: return False
        
        words, letters = {}, {}
        i = 0
        while i < n:
            word, letter = s[i], pattern[i]
            if word not in words and letter not in letters:
                words[word] = letter
                letters[letter] = word
            elif word not in words or letter not in letters:
                return False
            elif words[word]!=letter or letters[letter]!=word:
                return False
            i+=1
        
        return True