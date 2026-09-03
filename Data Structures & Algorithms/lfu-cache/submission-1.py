from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        self.key_to_val_freq = {}                 # key -> [value, freq]
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys (LRU within freq)

    def _bump_freq(self, key: int) -> None:
        value, freq = self.key_to_val_freq[key]

        # Remove key from current frequency bucket
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Add key to next frequency bucket
        new_freq = freq + 1
        self.freq_to_keys[new_freq][key] = None
        self.key_to_val_freq[key] = [value, new_freq]

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        value, _ = self.key_to_val_freq[key]
        self._bump_freq(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self._bump_freq(key)
            return

        # Evict LFU; if tie, evict LRU within min_freq bucket
        if self.size == self.capacity:
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]
            self.size -= 1

        # Insert new key with freq = 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
        self.size += 1