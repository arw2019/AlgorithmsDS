# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: 'TreeNode') -> str:
        """Encodes a tree to a single string."""
        vals = []
        def write(node):
            nonlocal vals
            if node:
                vals += [str(node.val)]
                write(node.left)
                write(node.right)
            else:
                vals += ['#']
        write(root)
        return ' '.join(vals)
                

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        vals = iter(data.split())
        def read():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = read()
                node.right = read()
                return node
        return  read()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
