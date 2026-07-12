class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])

        res = [intervals[0]]

        for start,end in intervals[1:]:

            prev = res[-1]
            if prev[1] >=  start:
                #merge
                res[-1][1] = max(prev[1],end)
            else:
                res.append([start,end])


        return res

        

