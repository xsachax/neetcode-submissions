class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for s, d, w in flights:
            adj[s].append((d, w))

        pq = [(0, src, 0)]  # (cost, node, stops)
        best = dict()       # (node, stops) -> cost

        while pq:
            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost  # found cheapest path to dst within limit

            if stops > k:
                continue

            for neighbour, edge_weight in adj[node]:
                new_cost = cost + edge_weight
                state = (neighbour, stops + 1)

                if state not in best or new_cost < best[state]:
                    best[state] = new_cost
                    heapq.heappush(pq, (new_cost, neighbour, stops + 1))
        return -1