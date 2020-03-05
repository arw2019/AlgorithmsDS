# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.gen = self._inorder(self.root)
        self.vals = deque()
        
    def _inorder(self, node):
        if not node: return None
        if node.left:
            yield from self._inorder(node.left)
        yield node.val
        if node.right:
            yield from self._inorder(node.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.vals.popleft() if self.vals else next(self.gen)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        try:
            nextVal = next(self.gen)
            self.vals.append(nextVal)
            return True
        except StopIteration:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
