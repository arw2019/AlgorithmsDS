class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = [float('-inf')]*3
        for n in nums:
            if n in top3: continue
            if n > top3[0]: top3 = [n] + top3[:2]
            elif n > top3[1]: top3[1], top3[2] = n, top3[1]
            elif n > top3[2]: top3[2] = n
        return top3[2] if top3[2] > float('-inf') else top3[0]
