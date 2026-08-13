import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}
        for src, dest, weight in times:
            adj[src].append((dest, weight))
        distances = {x: float('inf') for x in adj.keys()}
        distances[k] = 0
        pq = [(0, k)] # saved as (distance from a certain node, current node)

        while pq:
            current_distance_to_node, node = heapq.heappop(pq)
            
            if current_distance_to_node > distances[node]:
                continue

        
            for neighbour, edge_weight in adj[node]:
                distance = current_distance_to_node + edge_weight

                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(pq, (distance, neighbour))
        
        res = max(distances.values())
        return res if res < float('inf') else -1
