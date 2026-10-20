class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0]) - 1
        t = 0 
        b = len(matrix) - 1
        res = []

        '''matrix=[[1,2, 3, 4][
                    5, 6, 7, 8]
                [   9,10,11,12]]
        '''
        

        while l <= r and t <=b:


            #top row
            for i in range(l,r+1):
                res.append(matrix[t][i])

            t +=1

            #right col
            for i in range(t,b+1):
                res.append(matrix[i][r])

            r-=1

            if not (l <= r and t <=b):
                break

             

            #bottom row
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b -=1

            #left col
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])

            l +=1

        return res
