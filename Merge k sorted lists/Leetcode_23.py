# top 10%

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
       
        if not any(l for l in lists): return None 
        
        pq = []
        for idx, l in enumerate(lists):
            if l: heapq.heappush(pq, (l.val, idx))
    
        res = ListNode(0)
        cur = res
        while pq:
            _, idx = heapq.heappop(pq)
            cur.next = lists[idx]
            cur, lists[idx] = cur.next, lists[idx].next
            if lists[idx]: heapq.heappush(pq, (lists[idx].val, idx))
       
        return res.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
