# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        while cur:
            for _ in range(m):
                prev, cur = cur, cur.next
                if not cur: break
            if not cur: break
            for _ in range(n-1):
                cur = cur.next
                if not cur: break
            if cur:
                prev.next, cur = cur.next, cur.next
            elif prev:
                prev.next = None
                
        return head
