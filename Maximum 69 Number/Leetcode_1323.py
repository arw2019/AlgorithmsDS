class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        i = 0
        while i < len(digits) and digits[i] == '9':
            i+=1
        if i == len(digits): 
            return num
        else:
            digits[i] = '9'
            return int(''.join(digits))
