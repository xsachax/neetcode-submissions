import heapq

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.time = 0
        self.data = {}          # key -> [value, freq, last_used_time]
        self.heap = []          # (freq, last_used_time, key)

    def _touch(self, key: int):
        value, freq, _ = self.data[key]
        freq += 1
        self.time += 1
        self.data[key] = [value, freq, self.time]
        heapq.heappush(self.heap, (freq, self.time, key))

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        value = self.data[key][0]
        self._touch(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.data:
            self.data[key][0] = value
            self._touch(key)
            return

        if len(self.data) >= self.capacity:
            while self.heap:
                freq, ts, k = heapq.heappop(self.heap)
                if k in self.data and self.data[k][1] == freq and self.data[k][2] == ts:
                    del self.data[k]
                    break

        self.time += 1
        self.data[key] = [value, 1, self.time]
        heapq.heappush(self.heap, (1, self.time, key))
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)