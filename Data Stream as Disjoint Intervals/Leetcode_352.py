class SummaryRanges:
    def __init__(self):
        self.seen = set()
        self.start, self.end = dict(), dict()

    def addNum(self, val: int) -> None:
        """
        involves only add/delete ops into dictionaries and sets
        => O(1) time complexity
        """
        if val in self.seen:
            return
        self.seen.add(val)
        interval = [val, val]
        if val + 1 in self.start.keys():
            interval[1] = self.start[val + 1]
            self.start.pop(val + 1)
        if val - 1 in self.end.keys():
            interval[0] = self.end[val - 1]
            self.end.pop(val - 1)
        self.start[interval[0]] = interval[1]
        self.end[interval[1]] = interval[0]

    def getIntervals(self) -> List[List[int]]:
        """
        at each call intervals need to be sorted
        => O(klgk) where k is number of intervals
        """
        return sorted(self.start.items())


import bisect


class SummaryRanges:
    def __init__(self):
        self.seen = set()
        self.ends = [-float("inf"), float("inf")]
        self.starts = [-float("inf"), float("inf")]

    def addNum(self, val: int) -> None:
        """
        intervals are stored in a sorted array
        function includes insertions into that array
        => O(k) time complexity
        where k = number of intervals
        """
        if val in self.seen:
            return
        self.seen.add(val)
        i = bisect.bisect_left(self.starts, val) - 1
        if val - 1 == self.ends[i] and val + 1 == self.starts[i + 1]:
            del self.ends[i]
            del self.starts[i + 1]
        elif val - 1 == self.ends[i]:
            self.ends[i] += 1
        elif val + 1 == self.starts[i + 1]:
            self.starts[i + 1] -= 1
        else:
            self.ends.insert(i + 1, val)
            self.starts.insert(i + 1, val)

    def getIntervals(self) -> List[List[int]]:
        """
        O(k) time complexity
        intervals need to be retrieved from the sorted arrays each time
        but they are already in sorted order
        """
        return [[s, e] for s, e in zip(self.starts[1:-1], self.ends[1:-1])]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
