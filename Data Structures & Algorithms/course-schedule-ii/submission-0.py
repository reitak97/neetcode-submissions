class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses

    
        for a,b in prerequisites:
            adjList[b].append(a)
            inDegree[a] +=1
        
        q = deque()
        res = []
        #q = [0,2]
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
                res.append(i)

     
        canTake = 0
        #cycle if no indegree nodes with 0
        while q:
            curr = q.popleft()
            canTake +=1
            for nei in adjList[curr]:
                inDegree[nei] -=1
                if inDegree[nei] == 0:
                    q.append(nei)
                    res.append(nei)


        if numCourses != canTake:
            return []
        else:
            return res


    