# solve again
class TweetCounts:

    def __init__(self):
        self.tweet_dict = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweet_dict:
            self.tweet_dict[tweetName] = []
        self.tweet_dict[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        sec = 0
        
        if freq == "minute":
            sec = 60
        elif freq == "hour":
            sec = 3600
        # day
        else:
            sec = 86400
        
        int_num = (endTime-startTime)//sec + 1
        result = [0]*int_num
        
        for time in self.tweet_dict[tweetName]:
            if startTime<=time<=endTime:
                index = (time-startTime)//sec
                result[index] += 1
                
        return result

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)