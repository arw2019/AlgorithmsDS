# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def getLength(head: ListNode) -> int:
            """returns number of nodes in a linked list"""
            length, prev, cur = 0, None, head
            while cur:
                prev, cur = cur, cur.next
                length += 1
            return length
    
        def reverseList(head: ListNode) -> ListNode:
            """reverse linked list and return head of reversed list"""
            prevNode, curNode, nextNode = None, head, None
            while curNode:
                nextNode, curNode.next = curNode.next, prevNode
                prevNode, curNode = curNode, nextNode
            return prevNode
        
        def combineLists(node1: TreeNode, node2: TreeNode) -> None:
            """combines two linked lists in-place"""
            while node1 and node2:
                node1.next, node2.next, node1, node2 = node2, node1.next, node1.next, node2.next
        
        if not head: return
        
        N, cnt, cur = getLength(head), 0, head
        
        while cnt < N//2:
            cur = cur.next
            cnt += 1
        
        cur.next, rear = None, reverseList(cur.next)
        combineLists(head, rear)        