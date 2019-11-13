# top 2%
class SummaryRanges:

    def __init__(self):
        self.seen = set()
        self.start, self.end = dict(), dict()

    def addNum(self, val: int) -> None:
        if val in self.seen:
            return
        self.seen.add(val)
        interval = [val, val]
        if val + 1 in self.start.keys():
            interval[1] = self.start[val+1]
            self.start.pop(val+1)
        if val - 1 in self.end.keys():
            interval[0] = self.end[val-1]
            self.end.pop(val-1)
        self.start[interval[0]] = interval[1]
        self.end[interval[1]] = interval[0]
    
    def getIntervals(self) -> List[List[int]]:
        return sorted(self.start.items())

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()