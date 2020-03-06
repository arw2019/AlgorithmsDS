# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.val = None
        self.iterator = iterator
        
    def peek(self) -> int:
        if self.val is None:
            self.val = self.iterator.next()
        return self.val

    def next(self) -> int:
        if self.val is not None:
            tmp, self.val = self.val, None
            return tmp
        else:
            return self.iterator.next()

    def hasNext(self) -> bool:
        self.val = self.next()
        return self.val >= 0

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
