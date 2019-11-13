class Solution:
    def countAndSay(self, n: int) -> str:
        x = '1'
        for _ in range(n-1):
            x = ''.join(str(len(list(group))) + digit 
                       for digit, group in itertools.groupby(x))
        return x