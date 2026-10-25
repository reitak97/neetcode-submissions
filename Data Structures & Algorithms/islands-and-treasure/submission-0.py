class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        #nearest so use BFS
        #new bfs on each call so we need the new visited array
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        seen = set()
        #add all 0s to q first then do multi source bfs

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                for dr , dc in dirs:
                    nr,nc = r + dr, c+ dc
                    if (0<= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1 and (nr,nc) not in seen):
                        q.append((nr,nc))
                        seen.add((nr,nc))



            dist +=1


            