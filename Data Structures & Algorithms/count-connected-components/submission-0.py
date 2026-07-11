class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = n * [False]
        def dfs(node):
        
            for neighbor in adj[node]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    dfs(neighbor)

        res =0 

        for n in range(n):
            if visited[n] == False:
                visited[n] = True
                dfs(n)
                res +=1


        return res 
            
            






            
            
