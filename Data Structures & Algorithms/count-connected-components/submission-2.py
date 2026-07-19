class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)



        seen = set()
        def dfs(node):

            seen.add(node)

            for nei in adj[node]:
                if nei not in seen:
                    dfs(nei)



        for i in range(n):
            if i not in seen:
                dfs(i)
                res +=1

        return res        






            
            
