class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            

            qLen = len(q)
            #process all rotten at current level
            for _ in range(qLen):
                r,c = q.popleft()
                #try all directions
                for dr,dc in dir:
                    cr,cc = r + dr, c + dc
                    #check if bounds and fresh
                    if (cr in range(0,ROWS) 
                        and cc in range(0,COLS) 
                        and grid[cr][cc] == 1):
                            grid[cr][cc] = 2
                            q.append((cr,cc))
                            fresh -=1
            if q:
                time +=1
                        
                
                        
                


        if fresh == 0:
            return time
        return -1
