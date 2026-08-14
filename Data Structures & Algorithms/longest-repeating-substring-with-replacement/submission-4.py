from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0
        res = 0

        for r, v in enumerate(s):
            window[v]+=1
            while ((r-l+1) - max(window.values())) > k: # while # of non-majority chars > k
                window[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)

        return res