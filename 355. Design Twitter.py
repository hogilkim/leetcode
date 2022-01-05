#solve again

class Twitter:

    def __init__(self):
        self.followingId = defaultdict(set)
        self.posts = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        self.followingId[userId].add(userId)
        
        for followeeId in self.followingId[userId]:
            if followeeId in self.posts:
                index = len(self.posts[followeeId]) - 1
                count, tweetId = self.posts[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.posts[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingId[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingId[followerId]:
            self.followingId[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)