class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        t = text.split()
        ans, i = [], 0
        while i < len(t):
            try:
                i = t.index(first, i)
            except ValueError:
                break
            if i < len(t)-2 and t[i+1] == second:
                ans.append(t[i+2])
            i+=1
        return ans
