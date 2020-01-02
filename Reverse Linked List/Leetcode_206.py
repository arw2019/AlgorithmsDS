#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev, _next = head, None, None
        while cur:
            _next = cur.next
            cur.next = prev
            cur, prev = _next, cur
        return prev
            

# recursive solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head

        dummy = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return dummy
