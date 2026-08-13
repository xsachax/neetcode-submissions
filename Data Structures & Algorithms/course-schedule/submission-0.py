class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)
        visitedLoop = set()

        def dfs(course):
            if adj[course] == []: # no prereqs
                return True
            if course in visitedLoop: # found a loop
                return False

            visitedLoop.add(course)
            for p in adj[course]:
                if not dfs(p):
                    return False
            visitedLoop.remove(course)
            adj[course] = []
            return True

        


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True