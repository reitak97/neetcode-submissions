class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap of size k
        res = []
        heapq.heapify(res)

        for n in nums:
            heapq.heappush(res,n)

            if len(res) > k:
                heapq.heappop(res)


        #pop 
        return res[0]