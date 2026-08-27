class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        res = []
        while q:
            c = q.popleft()
            res.append(c)


            for n in adj[c]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
    

        return res[::-1] if len(res) == numCourses else []