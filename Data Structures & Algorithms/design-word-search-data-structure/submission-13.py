class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word): # end of word
                return curr.isEndOfWord
            c = word[i]
            if c == ".": # dfs all children
                return any(dfs(i+1, tn) for child, tn in curr.children.items())
            elif c in curr.children: # dfs single child
                return dfs(i+1, curr.children[c])
            else:
                return False

        
        return dfs(0, self.root)




        
