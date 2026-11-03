class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]



        def find(n):
            #base 
            if parent[n] == n:
                return n
            
            parent[n] = find(parent[n])
            return parent[n]
        
            


        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return 0   
            else:
                parent[p1] = p2
                return 1
        res = n
        for u,v in edges:
            res -= union(u,v)

        return res


        