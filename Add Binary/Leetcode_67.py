class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res_reversed = []
        a, b = map(list, [a, b])
        carry = 0
        while a or b or carry:
            cur = carry
            if a: cur += int(a.pop())
            if b: cur += int(b.pop())
            res_reversed += [cur % 2]
            carry = cur // 2
        return ''.join(map(str, res_reversed[::-1]))
