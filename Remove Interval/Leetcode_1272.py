class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        remove_left, remove_right = toBeRemoved
        for left, right in intervals:
            if right <= remove_left or left >= remove_right:
                res += [[left, right]]
            else:
                if left < remove_left:
                    res += [[left, remove_left]]
                if right > remove_right:
                    res += [[remove_right, right]]
        return res