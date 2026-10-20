class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        def coordToIdx(x,y):
            return (x*COLS) + y
        def idxToCoord(i):
            x = i//COLS
            y = i%COLS
            return (x,y)
        l = 0
        r = coordToIdx(ROWS-1,COLS-1)
        while l <=r:
            m = (l+r)//2
            x,y = idxToCoord(m)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = m-1
            else:
                l = m +1


        return False




