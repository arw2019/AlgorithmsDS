import bisect

class RangeModule:

    def __init__(self):
        self._intervals = []
        self.debug=True

    def addRange(self, start: int, end: int) -> None:
        leftSide = [i for i in self._intervals if i[1] < start]
        rightSide = [i for i in self._intervals if i[0] > end]
        if leftSide + rightSide != self._intervals:
            start = min(start, self._intervals[len(leftSide)][0])
            end = max(end, self._intervals[~len(rightSide)][1])
        self._intervals = leftSide + [[start, end]] + rightSide
        if self.debug: print(f'current set of ranges: {self._intervals}')
        
    def queryRange(self, start: int, end: int) -> bool:
        if self.debug: print(f'Query range: [{start},{end})')
        left_insert = bisect.bisect_left(self._intervals, [start, end])
        ans = False
        if left_insert > 0 :
            ans = ans or self._intervals[left_insert-1][1] >= end
            if self.debug: print(f'checked insertion range: {self._intervals[left_insert-1]}; result={ans}')
        if left_insert < len(self._intervals):
            if self.debug: print(f'checked insertion range: {self._intervals[left_insert]}; result={ans}')
            ans = ans or (self._intervals[left_insert][0] == start and self._intervals[left_insert][1] >= end)
        return ans

    def removeRange(self, start: int, end: int) -> None:
        left_insert = bisect.bisect_left(self._intervals, [start, end])
        right_insert = bisect.bisect_right(self._intervals, [start, end])
        if left_insert != right_insert:
            updated_intervals = self._intervals[:left_insert]
            i = left_insert
            while self._intervals[i][1] < end: 
                i+=1
            if i < right_insert and self._intervals[i][1] > end:
                updated_intervals.append([end, self._intervals[i][1]])
            updated_intervals += self._intervals[right_insert:]
            self._intervals = updated_intervals
        else:
            insert = left_insert
            if insert > 0 and self._intervals[insert-1][1] > start: 
                if self._intervals[insert-1][1] <= end:
                    self._intervals[insert-1][1]=start
                else:
                    self._intervals = self._intervals[:insert-1] + \
                                    [[self._intervals[insert-1][0], start]] + \
                                    [[end, self._intervals[insert-1][1]]] + \
                                    self._intervals[insert:]
            elif insert < len(self._intervals):
                self._intervals[insert][0] = max(end, self._intervals[insert][0])

   
        
        if self.debug: print(f'current set of ranges: {self._intervals}')
            
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
