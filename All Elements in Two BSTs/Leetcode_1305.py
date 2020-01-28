# correct but slow (TLE)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    
        debug = False

        def inorder(node: TreeNode):
            if not node: return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
            
        res = []
        
        iter1, iter2 = inorder(root1), inorder(root2)
        val1, val2 = None, None
        

        while True:
            if debug: print(res)
            if val1 is None:
                try:
                    val1 = next(iter1)
                except StopIteration:
                    if val2: res.append(val2)
                    return res + list(iter2)
            
            if val2 is None:
                try:
                    val2 = next(iter2)
                except StopIteration:
                    if val1: res.append(val1) 
                    return res + list(iter1)
            
            if val1 <= val2:
                if debug: print(f'val1: {val1}, val2={val2}')
                res.append(val1)
                val1 = None
            else:
                if debug: print(f'val1: {val1}, val2={val2}')
                res.append(val2)
                val2 = None
                
        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
