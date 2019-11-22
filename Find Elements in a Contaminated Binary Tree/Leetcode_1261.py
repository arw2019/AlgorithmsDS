# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.vals = set()
        def recover(node: TreeNode) -> None:
            if node.left:
                node.left.val = 2 * node.val + 1
                self.vals.add(node.left.val)
                recover(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                self.vals.add(node.right.val)
                recover(node.right)
        recover(self.root)

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
