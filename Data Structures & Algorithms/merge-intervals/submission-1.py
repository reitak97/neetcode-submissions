class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        res.append(intervals[0])
        for i in range(1,len(intervals)):

            #if overlapping
            if intervals[i][0] <= intervals[0][1]:
                #merge
                intervals[0][1] = intervals[i][1]
            else:
                res.append(intervals[i])


        return res

