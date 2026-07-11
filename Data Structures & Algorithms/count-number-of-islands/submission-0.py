class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands =0 
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    r, c = row + dr, col+ dc
                    if(r < 0 or c < 0 or r >=len(grid) or c >= len(grid[0]) or grid[r][c] == "0"):
                        continue
                    q.append((r,c))
                    grid[r][c] = "0"


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
        return islands
