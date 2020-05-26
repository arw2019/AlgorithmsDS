# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(N1 + N2) time where N1, N2 are lengths of inputs
# O(1) extra space 

# top 0.7%
class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev, cur = cur, nextNode
        return prev
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1, l2 = self.reverseList(l1), self.reverseList(l2)
        
        dummy = ListNode(-1)
        res = dummy
        carryover = 0
        while l1 or l2:
            cur = carryover
            if l1: 
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            cur, carryover = cur % 10, cur // 10
            res.next = ListNode(cur)
            res = res.next
        if carryover: res.next = ListNode(carryover)
        
        return self.reverseList(dummy.next)
