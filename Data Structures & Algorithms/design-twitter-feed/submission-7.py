from collections import deque, defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.idx, tweetId, userId))
        self.idx+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []

        for u in self.following[userId] | {userId}:
            if self.tweets[u]:
                idx, tweetId, userId = self.tweets[u][0]
                h.append((idx, tweetId, userId, 0)) # 0 is tracker index
        heapq.heapify_max(h)

        # grab the latest tweet from every user, then pop and repush the next latest tweet from that same user till we have 10 tweets.
        res = []
        i=0
        while h and i < 10:
            idx, tweetId, userId, trackerIdx = heapq.heappop_max(h)
            res.append(tweetId)
            if self.tweets[userId] and trackerIdx < len(self.tweets[userId])-1:
                idx, tweetId, userId = self.tweets[userId][trackerIdx+1]
                heapq.heappush_max(h, (idx, tweetId, userId, trackerIdx+1))
            i+=1
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
