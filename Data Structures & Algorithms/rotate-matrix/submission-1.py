class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r= len(matrix) - 1

        while l < r:
            #offset of i
            for i in range(r-l):
                t = l
                b = r


            

                #save top right
                tr = matrix[t+i][r]
                matrix[t+i][r] = matrix[t][l+i]

                #save bot right
                br = matrix[b][r-i]
                matrix[b][r-i] = tr

                #save bot left
                bl = matrix[b-i][l]
                matrix[b-i][l] = br

                tl = matrix[t][l+i]
                matrix[t][l+i] = bl

             
            l +=1
            r-=1



        