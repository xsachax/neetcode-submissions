from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        for destinations in adj.values():
            destinations.sort(reverse=True)
        
        route = []

        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())  # smallest destination
            route.append(airport)

        dfs("JFK")
        return route[::-1]
