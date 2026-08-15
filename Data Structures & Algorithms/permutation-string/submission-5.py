class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        wCount = [0] * 26

        for i in range(len(s1)): #initial counts
            s1Count[ord(s1[i]) - ord('a')]+=1
            wCount[ord(s2[i]) - ord('a')]+=1

            
        matches=0
        for i in range(26):
            if s1Count[i] == wCount[i]:
                matches+=1
        l=0
        for r in range(len(s1), len(s2)):
            # check for match
            if matches == 26:
                return True

            i1 = ord(s2[l]) - ord('a')
            i2 = ord(s2[r]) - ord('a')

            wCount[i1]-=1
            if s1Count[i1] == wCount[i1]:
                matches+=1
            elif s1Count[i1] == wCount[i1]+1:
                matches-=1

                
            wCount[i2]+=1            
            if s1Count[i2] == wCount[i2]:
                matches+=1
            elif s1Count[i2] == wCount[i2]-1:
                matches-=1 
            l+=1
            

        return matches == 26
