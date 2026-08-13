import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)} # i: [edge_weight, neighbour]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        pq = [[0, 0]]
        seen = set()
        res = 0
        
        while pq and len(seen) < N:
            dist, node = heapq.heappop(pq)
            if node in seen: 
                continue
            seen.add(node)
            res+=dist
            for neighbour in adj[node]:
                if neighbour[1] not in seen:
                    heapq.heappush(pq, neighbour)
        return res
