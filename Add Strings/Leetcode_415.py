# solution using itertools

from itertools import zip_longest
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        get_val = lambda char: ord(char) - 48
        cur, carry = [], 0
        for char1, char2 in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            carry += get_val(char1) + get_val(char2)
            cur += [carry%10]
            carry //= 10
        if carry: 
            cur += [str(carry)]
        return ''.join(str(c) for c in reversed(cur))
        

# same as below but work with strings directly

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, p = 0, 0 
        i1, i2 = len(num1)-1, len(num2)-1
        while i1>=0 or i2>=0:
            dig1 = int(num1[i1]) if i1>=0 else 0
            dig2 = int(num2[i2]) if i2>=0 else 0
            res += (dig1+dig2) * 10**p
            p+=1
            i1, i2 = i1-1, i2-1
        return str(res)

# convert strings to lists then pop from list and add

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        res, p = 0, 0 
        while num1 or num2:
            dig1 = int(num1.pop()) if num1 else 0
            dig2 = int(num2.pop()) if num2 else 0
            res += (dig1+dig2) * 10**p
            p+=1
        return str(res)
