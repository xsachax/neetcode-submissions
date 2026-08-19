from collections import deque, defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.idx, tweetId))
        self.idx+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []

        for u in self.following[userId] | {userId}:
            for t in self.tweets[u]:
                h.append(t)
        heapq.heapify_max(h)

        return [heapq.heappop_max(h)[1] for _ in range(min(10, len(h)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
