class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [False for _ in range(n)]
        for i in range(n):
            if leftChild[i]!=-1:
                if parents[leftChild[i]]:
                    return False
                else:
                    parents[leftChild[i]] = True
            if rightChild[i]!=-1:
                if parents[rightChild[i]]:
                    return False
                else:
                    parents[rightChild[i]] = True
        
        if sum(not parent for parent in parents) != 1:
            return False
        
        root = parents.index(False)
        seen, self.repeats = set(), False
        def dfs(i): 
            if i in seen:
                self.repeats = True
            if not self.repeats and i not in seen:
                seen.add(i)
                lc, rc = leftChild[i], rightChild[i]
                if lc != -1:
                    dfs(lc)
                if rc != -1:
                    dfs(rc)
            else:
                return False
        
        dfs(root)
        
        return not self.repeats and len(seen)==n
