class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for u,v in prerequisites:
            graph[u].append(v)


        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                return True
            

            visited.add(node)



            for nei in graph[node]:
                #check if cycle in nei
                if not dfs(nei):
                    return False

                    
            #just processed so clear
            visited.remove(node)
            graph[node] = []
            return True



        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True