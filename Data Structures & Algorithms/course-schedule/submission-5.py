class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #if no prerqe, base

        adjList = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            adjList[a].append(b)
        seen = set()

        def dfs(c):
            if c in seen:
                return False
            if adjList[c] == []:
                return True

            seen.add(c)
            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            seen.remove(c)
            adjList[c] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    