class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        seen = set([beginWord])
        neighbours = collections.defaultdict(list)
        q = deque([beginWord])
        dist = 1
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbours[pattern].append(word)
        

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return dist
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for w in neighbours[pattern]:
                        if w not in seen:
                            seen.add(w)
                            q.append(w)
            dist+=1  
        return 0