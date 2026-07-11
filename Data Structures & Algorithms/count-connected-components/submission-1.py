class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[]for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        seen = set()
        res = 0
        def dfs(n):
            for nei in adj[n]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)





        for i in range(n):
            if i not in seen:
                dfs(i)
                res +=1

    
        return res
