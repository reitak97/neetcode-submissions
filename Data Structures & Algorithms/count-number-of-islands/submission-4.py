class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r,c):
            
            stack = []
            stack.append((r,c))
            seen.add((r,c))

            while stack:
                r , c = stack.pop()
                for dr,dc in directions:
                    row, col = dr + r, dc + c
                    if (row >=0 and row < ROWS and col >= 0 and col < COLS
                    and grid[row][col] == "1" and (row,col) not in seen):
                        stack.append((row,col))
                        seen.add((row,col))

            
                

           

        for r in range(ROWS):
            for c in range(COLS):
                #start of new island
                if grid[r][c] == "1" and (r,c) not in seen:
                    
                    dfs(r,c)
                    res +=1

        return res