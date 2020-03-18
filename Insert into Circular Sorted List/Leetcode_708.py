"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        if not head:
            res = ListNode(insertVal)
            res.next = res
            return res
        
        prev, cur = head, head.next
        newNode = ListNode(insertVal)
        inserted = False
        
        while True:
            if prev.val <= insertVal <= cur.val \
                or prev.val > cur.val and (insertVal < cur.val or insertVal > prev.val):
                prev.next, newNode.next = newNode, cur
                inserted = True
                break
            prev, cur = cur, cur.next
            if cur is head:
                break
                
        if not inserted:
            prev.next, newNode.next = newNode, cur
            
        return head
