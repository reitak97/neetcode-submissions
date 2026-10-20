"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        cur = 0
        s = 0
        e = 0

        #start = [0,5,15]
        #end = [10,20,40]

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        while s < len(intervals):

            if start[s] < end[e]:
                cur +=1
                s +=1

            else:
                cur -=1
                e +=1


            res = max(res,cur)
        
        return res