from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ingoing = [[] for _ in range(numCourses)]
        outdegree = [0 for _ in range(numCourses)]
        for v, u in prerequisites:
            ingoing[u] += [v]
            outdegree[v] += 1
        
        order = [u for u in range(numCourses) if outdegree[u] == 0]
                
        count = 0
        while count != len(order):
            course = order[count]
            count += 1
            for u in ingoing[course]:
                outdegree[u] -= 1
                if outdegree[u] == 0:
                    order += [u]
        
        return order if count == numCourses else []