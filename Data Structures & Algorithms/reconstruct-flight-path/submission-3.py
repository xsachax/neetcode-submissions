class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, _ in tickets}

        for src, dst in sorted(tickets):
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            
            for i, v in enumerate(list(adj[src])):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()


        dfs("JFK")

        return res



        


        
