"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

# top 0.1% solution
from itertools import chain
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        work = sorted(chain(*schedule), key=lambda interval: interval.start)
        ans = []
        prev = work[0]
        for cur in work[1:]:
            if prev.end < cur.start:
                ans.append(Interval(prev.end, cur.start))
                prev = cur
            elif cur.end > prev.end:
                prev = cur
        return ans
