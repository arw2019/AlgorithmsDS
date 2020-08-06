class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        T = sum(calories[:k]) 
        i = 0
        while True:
            if T>upper:
                points += 1
            elif T<lower:
                points -= 1
            if i+k < len(calories):
                T -= calories[i]
                T += calories[i+k]
            else:
                break
            i += 1
        return points
