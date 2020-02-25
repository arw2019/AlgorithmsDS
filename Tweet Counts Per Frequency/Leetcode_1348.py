from collections import defaultdict
import bisect

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            timestep = 60
        elif freq == 'hour':
            timestep = 3600
        elif freq == 'day':
            timestep = 86400
        else:
            raise ValueError("Please enter a valid frequency.")
            
        res = []
        t1 = startTime
        while t1 <= endTime:
            t2  = min(endTime+1, t1+timestep)
            l = bisect.bisect_left(self.tweets[tweetName], t1)
            r = bisect.bisect_left(self.tweets[tweetName], t2)
            res += [r-l]
            t1 += timestep
            
        return res
            
            
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
