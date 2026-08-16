class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)


        seen = set()
        def dfs(i):
            if adj[i] == []:
                return True
            
            if i in seen:
                return False

            seen.add(i)
            for j in adj[i]:
                if dfs(j) == False:
                    return False

            seen.remove(i)
            adj[i] = []
            return True


        for c in adj.keys():
            if dfs(c) == False:
                return False

        return True


        