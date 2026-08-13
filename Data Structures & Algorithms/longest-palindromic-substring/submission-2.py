class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def getLongest(l, r):
            nonlocal resLen
            nonlocal res
            while l>=0 and r< len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1

        
        for i in range(len(s)):
            getLongest(i, i)    # odd length
            getLongest(i, i+1)  # even length
        
        return res


        