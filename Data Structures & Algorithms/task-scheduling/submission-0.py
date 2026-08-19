from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = [v for v in Counter(tasks).values()]
        heapq.heapify_max(h)
        q = deque() # for idle tasks, [count, nextAvailability]

        time = 0
        while h or q:
            time+=1

            if h: # take from heap
                c = heapq.heappop_max(h)
                c-=1
                if c>0:
                    q.append((c, time+n))

            else: # no ready tasks, fastforward to next available in queue
                time = q[0][1]

            if q and q[0][1] == time: # queued task is ready
                heapq.heappush_max(h, q.popleft()[0])
        return time