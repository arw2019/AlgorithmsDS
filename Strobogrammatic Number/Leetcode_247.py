# top 0.6%
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        arr = n%2 * list('018') or ['']
        while n > 1:
            n -=2
            arr = [n1 + n + n2 for n1, n2 in '00 11 88 69 96'.split(' ')[n<2:] for n in arr]
        return arr