# top 2%
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans, odds, evens = [], [], []
        for a in A:
            if a%2: odds += [a]
            else: evens += [a]
        for i in range(len(odds)):
            ans += [evens[i]] 
            ans += [odds[i]]
        return ans
