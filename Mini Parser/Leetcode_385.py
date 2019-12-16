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

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s: return NestedInteger() 
        stack = []
        n, sign = len(s), 1
        i = 0
        while i < len(s):
            if s[i] == '[': 
                stack.append(NestedInteger())
            elif s[i] == '-':
                sign = -1
            elif s[i].isdigit():
                digit = ''
                while i < n and s[i].isdigit():
                    digit += s[i]
                    i+=1
                cur = sign*int(digit)
                if not stack: stack.append(NestedInteger(cur))
                else:
                    stack[-1].add(NestedInteger(cur))
                sign = 1
                i-=1
            elif s[i] == ']':
                if i == len(s) - 1: break
                ni = stack.pop()
                if stack[-1].isInteger():
                    prev = stack.pop().getInteger()
                    stack.append(NestedList())
                    stack[-1].add(prev)
                    stack[-1].add(ni)
                else:
                    stack[-1].add(ni)
            i+=1
        return stack[0] if stack else NestedInteger()
