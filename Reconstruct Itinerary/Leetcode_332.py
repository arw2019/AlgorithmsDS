from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tkts = defaultdict(list)
        for origin, destination in tickets:
            tkts[origin].append(destination)
        
        self.trip = []
                
        def dfs(origin: str) -> bool:
            self.trip += [origin]
            if len(self.trip) == len(tickets)+1:
                return True
            for destination in sorted(list(tkts[origin])):
                tkts[origin].remove(destination)
                if dfs(destination): 
                    return True
                tkts[origin].append(destination)
            self.trip.pop()
            return False
        
        dfs('JFK')
        
        return self.trip
