class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for c,p in prerequisites:
            preMap[c].append(p)


        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            seen.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True