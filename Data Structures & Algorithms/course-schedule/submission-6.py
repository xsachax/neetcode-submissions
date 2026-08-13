class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        seen = set()

        def dfs(i: int) -> bool:
            if adj[i] == []:
                return True

            if i in seen:
                return False
            
            seen.add(i)
            for j in adj[i]:
                if not dfs(j):
                    return False
                    
            adj[j] = []
            seen.remove(i)
            return True
        
        for i in adj.keys():
            if dfs(i) == False:
                return False
        
        return True



    



       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # adj = {i:[] for i in range(numCourses)}
        # for c, p in prerequisites:
        #     adj[c].append(p)

        # visiting = set()

        # def dfs(num):
        #     if adj[num] == []: # no prereqs
        #         return True
        #     if num in visiting: #found a loop
        #         return False

        #     visiting.add(num)
        #     for prereq in adj[num]:
        #         if not dfs(prereq):
        #             return False
        #     visiting.remove(num)
        #     adj[num] = []
        #     return True

        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True




        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # adj = {i:[] for i in range(numCourses)}
        # for c, p in prerequisites:
        #     adj[c].append(p)
        # visitedLoop = set()

        # def dfs(course):
        #     if adj[course] == []: # no prereqs
        #         return True
        #     if course in visitedLoop: # found a loop
        #         return False

        #     visitedLoop.add(course)
        #     for p in adj[course]:
        #         if not dfs(p):
        #             return False
        #     visitedLoop.remove(course)
        #     adj[course] = []
        #     return True

        


        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True