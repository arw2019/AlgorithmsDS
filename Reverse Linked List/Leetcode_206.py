#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head

        if head.next is not None:
            dummy = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return dummy
        else: return head
