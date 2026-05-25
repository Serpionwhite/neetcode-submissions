class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        user_tweets = list(self.tweets[userId])
        for followeeId in self.following[userId]:
            user_tweets.extend(self.tweets[followeeId])

        top10 = heapq.nlargest(10, user_tweets, key=lambda x: x[0])
        return [tweetId for (_, tweetId) in top10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:


        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
