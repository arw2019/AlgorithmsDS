from collections import deque
class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = deque([str(i) for i in range(1,n+1)])
        def helper(curRound: 'deque(int)'):
            if len(curRound) == 2:
                return '(' + curRound[0] + ',' + curRound[-1] + ')'
            nextRound = deque()
            while curRound:
                team1, team2 = curRound.popleft(), curRound.pop()
                nextRound.append('(' + team1 + ',' + team2 + ')')
            return helper(nextRound)
        return helper(teams)
