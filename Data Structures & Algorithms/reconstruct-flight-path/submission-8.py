from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets):
        adj = defaultdict(deque)

        for src, dst in sorted(tickets):
            adj[src].append(dst)

        route = deque()

        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].popleft())
            route.appendleft(airport)

        dfs("JFK")
        return list(route)