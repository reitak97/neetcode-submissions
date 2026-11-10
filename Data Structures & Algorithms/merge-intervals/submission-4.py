class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
    
        res = [intervals[0]] #res = [[1,5]]
     

        for i in range(1,len(intervals)):
            last_end = res[-1][1] #5
            cur_start = intervals[i][0] #6
            if cur_start <= last_end:
                res[-1][1] = max(last_end,intervals[i][1])

            else:
                res.append(intervals[i])


        return res

       