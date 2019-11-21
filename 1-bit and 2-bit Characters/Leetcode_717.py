# top 1.5%
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx, char = 0, True
        while idx < len(bits):
            if bits[idx] == 1:
                flag = False
                idx += 2
            else:
                idx += 1
                flag = True
        return flag
        
# class Solution:
#     def isOneBitCharacter(self, bits: List[int]) -> bool:
#         if len(bits) == 1: return True
#         if len(bits) == 2: return bits[0] == 0
#         if bits[0] == 1:
#             return self.isOneBitCharacter(bits[2:])
#         return self.isOneBitCharacter(bits[1:])
