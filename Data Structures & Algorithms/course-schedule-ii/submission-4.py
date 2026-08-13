class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)
        visited, visiting = set(), set()
        res = []

        def dfs(course):
            if course in visiting: # found a loop
                return False
            if course in visited:
                return True

            visiting.add(course)
            for p in adj[course]:
                if not dfs(p):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            adj[course] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return res