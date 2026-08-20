from functools import cache
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for start, end, price in flights:
            adj[start].append((end, price))

        @cache
        def dfs(node, flights_remaining):
            if node == dst:
                return 0

            if flights_remaining == 0:
                return float("inf")

            cheapest = float("inf")

            for neighbor, price in adj[node]:
                cheapest = min(cheapest, price + dfs(neighbor, flights_remaining - 1))

            return cheapest

        result = dfs(src, k + 1)
        return result if result != float("inf") else -1