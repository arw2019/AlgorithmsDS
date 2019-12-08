# fast(top 1%) solution with only single passes through list1 and list2
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        best = float('inf')
        ind1 = {x:i for i, x in enumerate(list1)}
        for i, x in enumerate(list2):
            if x in ind1:
                cur = i + ind1[x]
                if cur == best: out.append(x)
                elif cur < best: best, out = cur, [x]
        return out

 # using set intersection
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        common = list(set(list1) & set(list2))
        n = len(common)
        minSum, ans = float('inf'), []
        for i,c in enumerate(common):
            idxSum = list1.index(c) + list2.index(c)
            if idxSum == minSum: 
                ans.append(c)
            elif idxSum < minSum:
                minSum, ans = idxSum, [c]
                
        return ans
