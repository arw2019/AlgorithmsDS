# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

# top 3%

from collections import defaultdict

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        self.d = defaultdict(int)
        self.max_depth = 1
        
        def dfs(nestedList: List[NestedInteger], depth: int) -> None:
            self.max_depth = max(self.max_depth, depth)
            for x in nestedList:    
                if x.isInteger():
                    self.d[depth] += x.getInteger()
                else:
                    dfs(x.getList(), depth+1)
        
        dfs(nestedList, 1)
        
        return sum([(self.max_depth-depth+1) * total for depth, total in self.d.items()])