from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {w:[] for w in wordList}

        d = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                d[pattern].append(w)

        print(d)
        
        

        seen = set()
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            seen.add(word)
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbour in d[pattern]:
                    if neighbour != word and neighbour not in seen:
                        q.append((neighbour, steps+1))
        return 0