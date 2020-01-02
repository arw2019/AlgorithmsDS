class Solution:
    def distanceBetweenBusStops(self, dist: List[int], start: int, destination: int) -> int:
        n = len(dist)
        if start > destination: start, destination = destination, start
        ck = sum(dist[start:destination])
        cck = sum(dist) - ck
        return min(ck, cck)
