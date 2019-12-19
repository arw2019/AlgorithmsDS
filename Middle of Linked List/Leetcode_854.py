# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        cur, i = head, 0
        while i!=cnt//2:
            i+=1
            cur = cur.next
        return cur
