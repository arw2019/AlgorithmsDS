from collections import defaultdict
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = set(dictionary)
        self.table = defaultdict(int)
        for word in self.dictionary:
            self.table[self.getAbbreviation(word)] += 1
        
    def getAbbreviation(self, word: str) -> str:
        return word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        
    def isUnique(self, word: str) -> bool:
        return self.table[self.getAbbreviation(word)] == 1 if word in self.dictionary \
            else self.getAbbreviation(word) not in self.table

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
