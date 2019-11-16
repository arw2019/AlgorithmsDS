# inspiration from https://leetcode.com/problems/design-linked-list/discuss/148773/Python-AC-short-and-simple-linked-list-solution
class ListNode:
    def __init__ (self, val: int = None):
        self.val = val
        self.next = None
        self.previous = None
    def __repr__(self):
        return "ListNode({val})".format(val=self.val)
    
class MyLinkedList:

    def __init__(self):
        self._head = ListNode(-1)
        self._tail = ListNode(-1)
        self._head.next = self._tail
        self._tail.previous = self._head
        self._num_list_elements = 0
        
    def _add(self, previousNode: ListNode, val: int) -> None:
        node = ListNode(val)
        node.previous, node.next = previousNode, previousNode.next
        node.previous.next = node.next.previous = node
        self._num_list_elements += 1
        
    def _remove(self, node: ListNode) -> None:
        node.previous.next, node.next.previous = node.next, node.previous
        self._num_list_elements -= 1
        
    def _forward(self, start: int, end: int, cur: ListNode) -> ListNode:
        while start != end:
            start += 1
            cur = cur.next
        return cur
    
    def _backward(self, start: int, end: int, cur: ListNode) -> ListNode:
        while start != end:
            start -= 1
            cur = cur.previous
        return cur
            

    def get(self, index: int) -> int:
        if 0 <= index <= self._num_list_elements // 2:
            return self._forward(0, index, self._head.next).val
        elif self._num_list_elements //2 < index < self._num_list_elements:
            return self._backward(self._num_list_elements-1, index, self._tail.previous).val
        return -1

    def addAtHead(self, val: int) -> None:
        self._add(self._head, val)

    def addAtTail(self, val: int) -> None:
        self._add(self._tail.previous, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self._num_list_elements // 2:
            self._add(self._forward(0, index, self._head.next).previous, val)
        elif self._num_list_elements //2 < index <= self._num_list_elements:
            self._add(self._backward(self._num_list_elements, index, self._tail).previous, val)  

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index <= self._num_list_elements // 2:
            self._remove(self._forward(0, index, self._head.next))
        elif self._num_list_elements //2 < index < self._num_list_elements:
            self._remove(self._backward(self._num_list_elements-1, index, self._tail.previous))        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)