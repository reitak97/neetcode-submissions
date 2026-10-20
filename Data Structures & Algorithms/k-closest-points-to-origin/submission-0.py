class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #create max heap limited to size k 
        minPoints = []
        for p in points:
            p_dist = math.sqrt( 
                (p[0]**2) + (p[1]**2)
            )
            heapq.heappush(minPoints,(-p_dist,p[0],p[1]))
            #if heap size exceeds k then pop largest dist
            if len(minPoints) > k:
                heapq.heappop(minPoints)

        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(minPoints)
            res.append([x,y])

        return res
