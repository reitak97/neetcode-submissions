class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #[0,0] -> [0,2]
        #[0,1] -> [1,2]
        #[0,2] -> [2,2]

       
        l = 0
        r = len(matrix) - 1
        while l < r:

            for i in range(r-l):
                t = l
                b = r

                #3
                topR = matrix[t+i][r]
                matrix[t+i][r] = matrix[t][l+i]

                botR = matrix[b][r-i]
                matrix[b][r-i] = topR

                botL = matrix[b-i][l]
                matrix[b-i][l] = botR

                matrix[t][l+i] = botL





            l +=1
            r -=1

        
