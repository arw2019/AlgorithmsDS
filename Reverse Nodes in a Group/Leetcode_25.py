# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseSubList(start: ListNode, end: ListNode) -> ListNode:
            cur, prev, next_ = start, None, None
            while cur is not end:
                next_ = cur.next
                cur.next = prev
                prev, cur = cur, next_
            return prev

        sentinel = ListNode(0)
        sentinel.next = head

        cur, prev = head, sentinel

        while cur:
            start = cur
            cnt = 0
            while cnt < k:
                if cur:
                    cur = cur.next
                    cnt += 1
                else:
                    prev.next = start
                    break
            else:
                node = reverseSubList(start, cur)
                prev.next, prev = node, start

        return sentinel.next
