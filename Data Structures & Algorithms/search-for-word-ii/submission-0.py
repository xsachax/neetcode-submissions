class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        root = TrieNode()
        for w in words:
            root.addWord(w)

        visited = set()
        res = set()


        def dfs(r, c, curr, word):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or board[r][c] not in curr.children:
                return
            curr = curr.children[board[r][c]]
            # at character now

            visited.add((r,c)) # visit
            word+=board[r][c] # add to word
            if curr.isEndOfWord:
                res.add(word)
            
            for dr, dc in DIRECTIONS:
                dfs(r+dr, c+dc, curr, word)
            visited.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

    
        return list(res)


        

