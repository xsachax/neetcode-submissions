# Prim

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # adj[i] contains [distance, neighbor] pairs.
        adj = {i: [] for i in range(N)}

        # Build the complete graph.
        for i in range(N):
            x1, y1 = points[i]

            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)

                # The graph is undirected.
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Start from point 0 at no cost.
        pq = [[0, 0]]       # [cost to add to curr mst, point idx]
        seen = set()
        res = 0

        while pq and len(seen) < N:
            dist, node = heapq.heappop(pq)

            # Multiple edges may lead to the same point.
            if node in seen:
                continue

            # Add this point and its connecting edge to the MST.
            seen.add(node)
            res += dist

            # Add candidate edges leaving this point.
            for neighbor in adj[node]:
                if neighbor[1] not in seen:
                    heapq.heappush(pq, neighbor)

        return res