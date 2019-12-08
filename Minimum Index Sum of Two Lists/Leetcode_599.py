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
