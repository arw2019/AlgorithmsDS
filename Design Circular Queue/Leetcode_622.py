# top 1%
class MyCircularQueue:

    def __init__(self, capacity: int):
        """
        Initialize your data structure here. Set the size of the queue to be capacity.
        """
        self._num_queue_elements = 0
        self._capacity = capacity
        self._front = 0
        self._rear = -1
        self._entries = [0] * capacity
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        
        if self.isFull(): 
            return False
        
        self._rear = (self._rear + 1) % self._capacity
        self._entries[self._rear] = value
        self._num_queue_elements += 1
        
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self._front = (self._front + 1) % self._capacity
        self._num_queue_elements -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self._entries[self._front] if self._num_queue_elements else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self._entries[self._rear] if self._num_queue_elements else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._num_queue_elements == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._num_queue_elements == self._capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()