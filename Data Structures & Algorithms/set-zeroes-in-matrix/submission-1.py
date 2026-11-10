class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        seen = set()
        def setZero(r,c):


            for row in range(len(matrix)):
                if (row,c) not in seen:
                    matrix[row][c] = 0
                    seen.add((row,c))


            for col in range(len(matrix[0])):
                if (r,col) not in seen:
                    matrix[r][col] = 0
                    seen.add((r,col))


        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                if matrix[r][c] == 0 and (r,c) not in seen:
                    setZero(r,c)
