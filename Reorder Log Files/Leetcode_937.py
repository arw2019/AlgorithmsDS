class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs, digitLogs = [], []
        for log in logs:
            identifier, words = log.split(' ', 1)
            if words[0].isalpha():
                letterLogs.append([identifier, words])
            else:
                digitLogs.append([identifier, words])
        order = sorted(letterLogs, key=lambda x: (x[1], x[0])) + digitLogs
        return [' '.join(log) for log in order]
