import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # textbook djikstra

        adj = {i:[] for i in range(1, n+1)}
        for src, dest, weight in times:
            adj[src].append((dest, weight))

        best_distances = {x: float('inf') for x in adj.keys()}
        best_distances[k] = 0

        h = [(0, k)]
        while h:
            curr_dist, node = heapq.heappop(h)
            if best_distances[node] < curr_dist: #already found a shorter path
                continue
            for n, w in adj[node]:
                new_distance = curr_dist+w
                if new_distance < best_distances[n]:
                    best_distances[n] = new_distance
                    heapq.heappush(h, (new_distance, n))
        
        
        res = max(best_distances.values())
        return res if res < float('inf') else -1