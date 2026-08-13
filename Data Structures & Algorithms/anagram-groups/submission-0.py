class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for a in strs:
            sorted_anagram = ''.join(sorted(a))
            if sorted_anagram in groups:
                groups[sorted_anagram].append(a)
            else:
                groups[sorted_anagram] = [a]
        
        return [g for g in groups.values()]