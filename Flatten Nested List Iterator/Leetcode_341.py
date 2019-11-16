# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList: 'NestedInteger'):
        def unfold(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in unfold(x.getList()):
                        yield y
        self.unfold = unfold(nestedList)
            
    def next(self) -> int:
        return self.val 

    def hasNext(self) -> bool:
        try:
            self.val = next(self.unfold)
            return True
        except StopIteration:
            return False
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())