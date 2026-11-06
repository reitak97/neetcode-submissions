class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for i in range(numCourses)] #directed graph

        inDegree = [0] * numCourses #[1,0]
        for u,v in prerequisites:
            inDegree[u] +=1
            adjList[v].append(u)


        q = deque() #[1]
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        canTake = 0
        while q:
            canTake +=1
            curr = q.popleft()
            for nei in adjList[curr]:
                inDegree[nei] -=1
                if inDegree[nei] == 0:
                    q.append(nei)
        return True if canTake == numCourses else False




            

            