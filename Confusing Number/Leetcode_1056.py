# top 0.8%
class Solution:
    def confusingNumber(self, N: int) -> bool:
        rotate = {0:0,1:1,6:9,8:8,9:6}
        Nr, n, i = 0, N, 0
        while n:
            n, digit = n //10, n%10
            if digit not in rotate: 
                return False
            Nr = Nr * 10 + rotate[digit]
            i += 1
        return N != Nr

# class Solution:
#     def confusingNumber(self, N: int) -> bool:
#         rotate = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
#         Nr = ''
#         for digit in str(N):
#             if digit not in rotate: 
#                 return False
#             Nr += rotate[digit]
#         return str(N) != Nr[::-1]