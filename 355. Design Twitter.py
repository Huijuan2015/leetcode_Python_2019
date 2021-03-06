class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.follower = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.timer = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append((self.timer, tweetId))
        self.timer -= 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweets = self.tweets[userId][:]
        res = []
        # print self.tweets[userId], tweets, self.follower[userId]
        for p in self.follower[userId]:
            if p != userId:
                tweets.extend(self.tweets[p])
        heapq.heapify(tweets)
        while tweets and len(res) < 10:
            res.append(heapq.heappop(tweets)[1])
        return res  

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)