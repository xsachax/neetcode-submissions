from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            window[s[r]]+=1
            othersCount = r-l+1 - max(window.values())
            if othersCount > k:
                window[s[l]]-=1
                l+=1
            else:
                res = max(res, r-l+1)
        return res
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
        # count = {}
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)

        #     if (r-l+1) - max(count.values()) > k:
        #         count[s[l]] -=1
        #         l+=1
        #     res = max(res, (r-l+1))
        # return res
        
