# top 1.6%
import bisect
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        """ 
        N = no. successful bookings
        O(lgN) complexity for unsuccessful booking [binary search in self.events]
        O(N) complexity for successful booking
        If there are a lot of successful calls to the function an alternative DS 
        should be used to store events (e.g. a balanced BST) so that insertion
        is less costly.
        """
        idx = bisect.bisect_right(self.events, (start, end))
        if idx != 0 and self.events[idx-1][1] > start: 
            return False
        if idx != len(self.events) and self.events[idx][0] < end: 
            return False
        bisect.insort(self.events, (start, end))
        return True
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
