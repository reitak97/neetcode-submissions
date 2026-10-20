class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = [False] * len(matrix)
        cols = [False] * len(matrix[0])

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True


        for i in range(len(rows)):
            if rows[i]:
                for c in range(len(matrix[0])):
                    matrix[i][c] = 0
        for i in range(len(cols)):
            if cols[i]:
                for r in range(len(matrix)):
                    matrix[r][i] = 0

        
        