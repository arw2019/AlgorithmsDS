# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        if head is None: return 
        
        linkedList, cur = [], head
        
        while cur:
            linkedList.append(cur)
            cur = cur.getNext()
                        
        for node in linkedList[::-1]:
            node.printValue()

 
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        def func(node: 'ImmutableListNode') -> List[int]:
            if node is None: 
                return []
            else:
                return func(node.getNext()) + [node.printValue()]
      
        return func(head)
