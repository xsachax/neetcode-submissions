class Solution:
    def minWindow(self, s: str, t: str) -> str:
        w = collections.defaultdict(int)
        tw = collections.defaultdict(int)
        for c in t:
            tw[c]+=1
        l=0
        minLen = float('inf')
        res = ""

        def isValidInWindow():
            for k, v in tw.items():
                if w[k] < v: 
                    return False
            else:
                return True
            
        for r in range(len(s)):
            w[s[r]]+=1
            while isValidInWindow():
                minLen = min(minLen, r-l+1)
                if (r-l+1) == minLen:
                    res = s[l:r+1]
                w[s[l]]-=1
                l+=1
        
        return res

                
        