class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        
        depth, cur, N = 0,  0, len(seq)
        
        # compute depth of seq
        for char in seq:
            if char == '(':
                cur += 1
            else:
                cur -= 1
            depth = max(depth, cur)
        
        # split seq "by half"
        # credit to lee215's post for reverse order of assignments in if/else 
        ans = [0] * N
        for i, char in enumerate(seq):
            if char == '(':
                cur += 1
                ans[i] = int(cur > depth/2)
            else:
                ans[i] = int(cur > depth/2)
                cur -= 1
        
        return ans
