# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        arr, d, inf = [0], defaultdict(list), float('inf')
        d[0].append(0)
        cur, cumsum = head, 0
        while cur: 
            cumsum += cur.val
            arr.append(cur.val)
            d[cumsum].append(len(arr))
            if len(d[cumsum]) > 1 and arr[d[cumsum][-2]] < inf:
                for j in range(d[cumsum][-2], d[cumsum][-1]):
                    arr[j] = inf
            cur = cur.next
        newHead = None
        
        for idx, val in enumerate(arr):
            if idx == 0: continue
            if val < inf:
                if not newHead: 
                    newHead = ListNode(val)
                    cur = newHead
                else: 
                    cur.next = ListNode(val)
                    cur = cur.next
        return newHead
