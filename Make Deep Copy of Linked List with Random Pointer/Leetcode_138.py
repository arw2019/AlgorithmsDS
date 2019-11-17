"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# O(N) time, O(1) space
# inspiration from liaison's post in the Discussion

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        cur = head
        
        while cur:
            copy = Node(cur.val, cur.next, None)
            cur.next = copy
            cur = copy.next
        
        cur = head
        while cur:
            cur.next.random = cur.random and cur.random.next
            cur = cur.next.next
            
        cur = head
        
        copy = copy_head = head and head.next
        while cur:
            cur.next = cur = copy.next
            copy.next = copy = cur and cur.next
        
        return copy_head

# O(N) time, O(N) space
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = defaultdict(lambda : Node(None, None, None))
        d[None] = None
        cur = head
        while cur:
            d[cur].val = cur.val
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]