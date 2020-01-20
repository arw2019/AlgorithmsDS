# Leetcode Problem 943: Find the Shortest Substring 
# credit: https://leetcode.com/problems/find-the-shortest-superstring/discuss/195487/python-bfs-solution-with-detailed-explanation(with-extra-Chinese-explanation)
from collections import deque

class Solution: 
    def shortestSubstring(self, A: 'List[str]') -> str: 
            
        def getDistance(s1: str, s2: str) -> int:
            """
            Computes saved length when placing s2 
            immediately behind s1
            """
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1)-i
            return 0

        def pathToStr(path: List[int]) -> str:
            """
            Concatenates strings into superstring.
            Chars are added as specified by path.
            """
            res = A[path[0]]
            for i in range(1, len(path)):
                res += A[path[i]][G[path[i-1]][path[i]]:]
            return res

        """
        Generate the graph.
        weight between words w1, w2 is number of 
        saved characters when concatenating w1+w2.
        """
        n = len(A)
        G = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                G[i][j] = getDistance(A[i], A[j])
                G[j][i] = getDistance(A[j], A[i])

        d = [[0]*n for _ in range(1<<n)]
        Q = deque([(i, 1<<i, [i], 0) for i in range(n)]) 
        l = -1
        P = []
        while Q:
            node, mask, path, dis = Q.popleft()
            if dis < d[mask][node]: continue
            if mask == (1<<n) - 1 and dis > l:
                P, l = path, dis
                continue
            for i in range(n):
                next_mask = mask | (1<<i)
                """
                First check that every node is traversed only once.
                Secondly do a greedy check. If we don't save more characters
                from the new configuration, we need not consider it further.
                """
                if next_mask != mask and d[mask][node] + G[node][i] >= d[next_mask][i]:
                    d[next_mask][i] = d[mask][node] + G[node][i]
                    Q.append((i, next_mask, path+[i], d[next_mask][i]))

        return pathToStr(P)

s = Solution()
input_1 = ["alex","loves","leetcode"]
result_1 = s.shortestSubstring(input_1)
print(result_1)

input_2 = ["catg","ctaagt","gcta","ttca","atgcatc"]
result_2 = s.shortestSubstring(input_2)
print(result_2)