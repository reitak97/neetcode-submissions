class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for a,b in prerequisites:
            inDegree[a] +=1
            adjList[b].append(a)

        q = deque()
        for i in range (len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)

        canTake = 0

        while q:
            curr = q.popleft()
            canTake +=1
            for nei in adjList[curr]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)




        return canTake == numCourses
