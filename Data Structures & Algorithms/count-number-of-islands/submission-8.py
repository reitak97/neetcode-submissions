class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        seen = set()
        def dfs(r,c):
            if ((r,c) in seen or r < 0 or r >= ROWS or c < 0 or c>=COLS or grid[r][c] == "0"):
                return
            
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c)not in seen:
                    dfs(r,c)
                    res +=1
        
        return res