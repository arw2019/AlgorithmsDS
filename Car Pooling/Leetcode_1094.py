class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: (x[1], x[2]))
        print(trips)
        heap = []
        tot = 0
        for num, start, end in trips:
            while heap and heap[0][0] <= start:
                tot -= heapq.heappop(heap)[1]
            tot += num
            if tot > capacity: return False
            heapq.heappush(heap, (end, num))
        return True