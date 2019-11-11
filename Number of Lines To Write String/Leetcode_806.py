# top 2%
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        d = {}
        for char in "abcdefghijklmnopqrstuvwxyz":
            d[char] = widths[(ord(char) - ord('a'))]
        
        lines, cur_width = 0, 0
        for char in S:
            if cur_width + d[char] <= 100:
                cur_width += d[char]
            else:
                lines += 1
                cur_width = d[char]
                
        if cur_width: lines += 1
            
        return  lines, cur_width
