from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        pq = []
        [heappush(pq, (l.val, i)) for i,l in enumerate(lists) if l]
            
        res = ListNode(float('-inf'))
        cur = res
        
        while pq:
            _, i = heappop(pq)
            cur.next = lists[i]
            cur, lists[i] = cur.next, lists[i].next
            if lists[i]: heappush(pq, (lists[i].val, i))
    
        return res.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
