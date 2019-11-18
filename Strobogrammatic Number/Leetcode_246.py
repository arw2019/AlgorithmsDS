class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo = {'0': '0', '1': '1', '6':'9',  '8':'8', '9':'6'}
        upsideNum = ''
        for i, digit in enumerate(num):
            if digit not in strobo: return False
            upsideNum += strobo[digit]
        return upsideNum[::-1] == num