# O(N) time, O(1) space
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurence = {char: i for i, char in enumerate(S)}
        ans, cur_start, cur_break = [], 0, last_occurence[S[0]]
        for idx, char in enumerate(S):
            cur_break = max(cur_break, last_occurence[char])
            if cur_break == idx:
                ans += [cur_break-cur_start+1]
                cur_start = idx+1
        return ans
    

# O(N) time, N=len(S)
# O(L) space, L = length of alphabet
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {}
        for i, char in enumerate(S):
            d[char] = i
        ans = []
        start = 0
        cur, finished = set(), set()
        for i, char in enumerate(S):
            if d[char] == i: 
                finished.add(char)
            cur.add(char)
            if cur == finished:
                ans += [i+1-start]
                start = i+1
        return ans
