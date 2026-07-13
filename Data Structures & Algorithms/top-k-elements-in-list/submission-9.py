class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create frequency counter
        freqC ={}
        for n in nums:
            freqC[n] = 1 + freqC.get(n,0)

        heap = []
        for key,value in freqC.items():
            heapq.heappush(heap,[value,key])
            if len(heap) > k:
                heapq.heappop(heap)
        

        res = []
        for i in range(k):
        
            res.append(heapq.heappop(heap)[1])

        return res