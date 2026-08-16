class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        # expand window till we have all matches
        # shrink window while valid
        # once no longer valid, re-expand till valid again
        # repeat
        tCount = [0] * 52
        wCount = [0] * 52
        res = ""
        resLen = float('inf')

        for i, char in enumerate(t):
            if 'a' <= char <= 'z':
                tCount[ord(t[i]) - ord('a')]+=1
            if 'A' <= char <= 'Z':
                tCount[ord(t[i]) - ord('A')+26]+=1

        have = 0
        need = len(set(t))
        l=0
        currWindowValid = False
        for r, char in enumerate(s):
            if 'a' <= char <= 'z':
                i = ord(s[r]) - ord('a')
            if 'A' <= char <= 'Z':
                i = ord(s[r]) - ord('A')+26
            wCount[i]+=1
            if tCount[i]>0: # if the letter is in t
                if wCount[i] == tCount[i]: # valid match
                    have+=1  

            while have == need:
                if (r-l+1) < resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                if 'a' <= s[l] <= 'z':
                    i = ord(s[l]) - ord('a')
                if 'A' <= s[l] <= 'Z':
                    i = ord(s[l]) - ord('A')+26
                wCount[i]-=1
                if wCount[i]+1 == tCount[i]: # lost 1 x 'have'
                    have-=1
                l+=1
                        
        return res

        