class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        window = set()
        l = 0

        for r, v in enumerate(s):
            while v in window:
                window.remove(s[l])
                l+=1
            window.add(v)
            maxLen = max(maxLen, len(window))
        return maxLen
        