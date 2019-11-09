# iterative stack solution
# top 0.5% 
class Solution:
    def decodeString(self, s: str) -> str:
        digits = set("0 1 2 3 4 5 6 7 8 9".split(" "))
        stack , num, cur = [], 0, ""
        for char in s:
            if char == '[':
                stack += [cur] + [num]
                cur, num = "", 0
            elif char == ']':
                k = stack.pop()
                prev = stack.pop()
                cur = prev + k * cur
            elif char in digits:
                num = 10*num + int(char)
            else:
                cur += char
        return cur

# recursive solution
# correct but somewhat slow (top 30%)
# class Solution:
#     def __init__(self):
#         self._i = 0
#     def decodeString(self, s: str) -> str:
#         result = ""
#         n = len(s)
#         digits = set("0 1 2 3 4 5 6 7 8 9".split(" "))
#         while self._i < n and s[self._i]!=']':
#             if not s[self._i] in digits:
#                 result += s[self._i]
#                 # print('if', result)
#                 self._i += 1
#             else:
#                 k = 0
#                 while self._i < n and s[self._i] in digits:
#                     k = k*10 + int(s[self._i])
#                     self._i+=1
#                 self._i+=1
#                 t = self.decodeString(s)
#                 self._i+=1
#                 result += k * t
#         return result