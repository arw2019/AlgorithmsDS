# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # unless both l1 and l2 are non-null there is little to do
        if not(l1 and l2):
            return l1 if l1 else l2
        
        res = ListNode(0) # sentinel node
        cur, curLeft, curRight = res, l1, l2
        
        while curLeft and curRight:
            # while there are unprocessed nodes in both lists
            # pick the node with smaller value
            # and advance pointers
            if curLeft.val <= curRight.val:
                curLeft, cur.next = curLeft.next, curLeft
            else:
                curRight, cur.next = curRight.next, curRight
            cur = cur.next
        
        # attach remainder
        if curLeft:
            cur.next = curLeft
        elif curRight:
            cur.next = curRight
            
        return res.next
