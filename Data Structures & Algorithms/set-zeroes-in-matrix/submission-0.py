class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        def setZero(r,c):

        #1,1,

            for row in range(len(matrix)):
                matrix[row][c] = 0


            for col in range(len(matrix[0])):
                matrix[r][col] = 0


        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                if matrix[r][c] == 0:
                    zeros.append((r,c))


        for r,c in zeros:
            setZero(r,c)