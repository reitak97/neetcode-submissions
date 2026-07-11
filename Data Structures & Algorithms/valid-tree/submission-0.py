class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

      
        seen = set()

        def dfs(n,prev):
           
            if n in seen:
                return False
            
            seen.add(n)

            for nei in adjList[n]:
                if nei == prev:
                    continue
                if not dfs(nei,n):
                    return False

            return True

        return dfs(0,-1) and len(seen) == n



       