# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sentinel = ListNode(float('-inf'))
        original = head
        while original:
            prev, cur = sentinel, sentinel.next
            while cur and cur.val <= original.val:
                prev, cur = cur, cur.next
            tmp, original = original, original.next
            prev.next, tmp.next = tmp, cur
        return sentinel.next
