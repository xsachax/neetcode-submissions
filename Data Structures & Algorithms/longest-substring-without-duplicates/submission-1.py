class Solution:
    from collections import defaultdict
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = defaultdict(int)
        res = 0

        for r, v in enumerate(s):
            window[v]+=1
            while window.get(v, 0) > 1:
                window[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # maxLen = 0
        # window = set()
        # l = 0

        # for r, v in enumerate(s):
        #     while v in window:
        #         window.remove(s[l])
        #         l+=1
        #     window.add(v)
        #     maxLen = max(maxLen, len(window))
        # return maxLen
        