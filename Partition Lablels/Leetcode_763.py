class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d, dq = dict(), collections.deque()
        for i, char in enumerate(S):
            if char not in d.keys(): 
                d[char] = [i, i]
                dq.append(char)
            elif i > d[char][1]: d[char][1] = i
        
        ans = []
        while dq:
            char1 = dq.popleft()
            start, end = d[char1][0], d[char1][1]
            while dq:
                char2 = dq.popleft()
                if d[char2][1] <= end or d[char2][0] < end:
                    end = max(end, d[char2][1])
                else:
                    dq.appendleft(char2)
                    ans.append(end-start+1)
                    start, end = None, None
                    break
        if start is not None: ans.append(end-start+1)
        return ans
