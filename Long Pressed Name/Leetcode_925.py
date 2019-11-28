class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        j = 0 # index of character in name we're looking at
        
        for i, char in enumerate(typed):
            if j == len(name): 
                return not typed[i:] or all(char == name[-1] for char in typed[i:])
            elif char == name[j]:
                j+=1
            elif char == name[j-1]:
                continue
            else:
                return False
        
        return j == len(name)