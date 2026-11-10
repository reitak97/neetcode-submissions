class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0

        newIntervals = []
        newIntervals.append(intervals[0])

        for i in range(1,len(intervals)):
            if intervals[i][0] < newIntervals[-1][1]:
                res +=1
            
            else:
                newIntervals.append(intervals[i])
            
        return res

