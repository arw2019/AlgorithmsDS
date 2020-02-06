from itertools import accumulate
import operator

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        bestOne, bestPair, bestTriplet = 0, [0, k], [0, k, 2*k] 
        sums = [sum(nums[i:i+k]) for i in range(0, 3*k, k)]
        bestSums = list(accumulate(sums, operator.add))
        curIdx = [1, k+1, 2*k+1]
        while curIdx[2] + k <= len(nums):
            sums = [sums[i] - nums[curIdx[i]-1] + nums[curIdx[i]+k-1] for i in range(3)]
            if sums[0] > bestSums[0]:
                bestOne, bestSums[0] = curIdx[0], sums[0]
            if bestSums[0] + sums[1] > bestSums[1]:
                bestPair = [bestOne, curIdx[1]]
                bestSums[1] = bestSums[0] + sums[1]
            if bestSums[1] + sums[2] > bestSums[2]:
                bestTriplet = bestPair + [curIdx[2]]
                bestSums[2] = bestSums[1] + sums[2]
            curIdx = [idx + 1 for idx in curIdx]
        return bestTriplet
