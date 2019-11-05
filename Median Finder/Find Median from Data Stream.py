class MedianFinder:

    import heapq
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = False
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)
        
        

    def addNum(self, num: int) -> None:
        num = float(num)
        # load new number into the heaps
        if self.median == False:
            self.median = num
            heapq.heappush(self.maxheap, -num)
        elif num < self.median:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
            
        # work out the median
        #if lengths of maxheap and minheap are equal
        if len(self.maxheap) == len(self.minheap):
            larger = -heapq.heappop(self.maxheap)
            smaller = heapq.heappop(self.minheap)
            self.median = (larger + smaller)/2
            heapq.heappush(self.maxheap, -larger)
            heapq.heappush(self.minheap, smaller)
        else:
            #if lengths of maxheap and minheap differ by 1
            if len(self.maxheap) == len(self.minheap) + 1:
                self.median = -heapq.heappop(self.maxheap)
                heapq.heappush(self.maxheap, -self.median)
            elif len(self.minheap) == len(self.maxheap) + 1:
                self.median = heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, self.median)
            # if lengths of maxheap and minheap differ by more than 1
            if len(self.maxheap) == len(self.minheap) + 2:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                larger = -heapq.heappop(self.maxheap)
                smaller = heapq.heappop(self.minheap)
                self.median = (larger + smaller)/2
                heapq.heappush(self.maxheap, -larger)
                heapq.heappush(self.minheap, smaller)
            if len(self.minheap) == len(self.maxheap) + 2:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                larger = -heapq.heappop(self.maxheap)
                smaller = heapq.heappop(self.minheap)
                self.median = (larger + smaller)/2
                heapq.heappush(self.maxheap, -larger)
                heapq.heappush(self.minheap, smaller)
                
        #print(self.maxheap, self.minheap, self.median)

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
