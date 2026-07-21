class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            #non overlapping and new comes before
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]


            #non overlaping new and comes after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            #overlapping
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res