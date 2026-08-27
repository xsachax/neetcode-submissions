from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[course].append(prereq)
            indegree[prereq]+=1




        q = deque()
        for course_number, ind in enumerate(indegree):
            if ind == 0:
                q.append(course_number)
        
        count=0

        while q:
            c = q.popleft()
            count+=1

            for n in adj[c]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
    

        return count == numCourses
        

