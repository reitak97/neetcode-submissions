class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adjList = [[] for _ in range(n)]

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        seen = set()
        def dfs(i):
            seen.add(i)
            for nei in adjList[i]:
                if nei not in seen:
                    dfs(nei)


        for i in range(n):
            if i not in seen:
                dfs(i)
                res +=1


        return res


    





            
            
