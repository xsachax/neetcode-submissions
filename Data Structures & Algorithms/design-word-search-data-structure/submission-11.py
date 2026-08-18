class WordDictionary:

    def __init__(self):
        self.d = {}
        

    def addWord(self, word: str) -> None:
        curr = self.d
        for i, c in enumerate(word):
            if c not in curr:
                curr[c] = {}
            if i == len(word)-1: # end of word
                curr[c]["is_end"] = True
                return
            curr = curr[c]
        

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                if curr.get("is_end", False):
                    return True
                else:
                    return False

            c = word[i]
            if c == ".":
                return any(dfs(i+1, v) for k, v in curr.items() if k != "is_end")
            elif c in curr:
                return dfs(i+1, curr[c])
            else:
                return False


        return dfs(0, self.d)


            
