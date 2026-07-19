class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        ROWS =len(heights)
        COLS = len(heights[0])

        res= []

        def dfs(r,c,visit,prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or prev > heights[r][c]:
                return
            
            visit.add((r,c))

            #run on four directions
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        

        for i in range(ROWS):
            #first col
            dfs(i,0,pac,heights[i][0])

            #last col
            dfs(i,COLS-1,atl,heights[i][COLS-1])

        for i in range(COLS):
            dfs(0,i,pac,heights[0][i])
            dfs(ROWS-1,i,atl,heights[ROWS-1][i])





        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])


        return res

