class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #undirect ajd list
        res = 0

        #run dfs/bfs on each and mark as visited
        adjList = [[] for _ in range(n)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        seen = set()
        def bfs(i):
            q = deque([i])
            seen.add(i)
            while q:
                cur = q.popleft()
                for nei in adjList[cur]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)


        for i in range(n):
            if i not in seen:
                bfs(i)
                res +=1

        return res


    





            
            
