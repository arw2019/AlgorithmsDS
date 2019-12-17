class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        
        parent = {}
        
        
        def find(char: str) -> str:
            if char not in parent: return char
            parent[char] = find(parent[char])
            return parent[char]
        
        def union(char1: str, char2: str) -> None:
            root1, root2 = find(char1), find(char2)
            if root1 > root2: parent[root1] = root2
            elif root2 > root1: parent[root2] = root1
        
        for i in range(len(A)):
            union(A[i], B[i])
                        
        res = ''
        
        for char in S:
            res += find(char)
        
        return res
