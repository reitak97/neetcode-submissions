class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #[0,0] -> [0,2]
        #[0,1] -> [1,2]
        #[0,2] -> [2,2]

        l = 0
        r = len(matrix)-1

        while l <r:
            for i in range(r-l):
                t,b = l,r
                #save top right 
                topRight = matrix[t+i][r]
                #move top left to top right
                matrix[t+i][r] = matrix[t][l+i]
                bottomRight = matrix[b][r-i]
                matrix[b][r-i] = topRight
                bottomLeft = matrix[b-i][l]
                matrix[b-i][l] = bottomRight
                matrix[t][l+i] = bottomLeft
            r-=1
            l+=1  


        
