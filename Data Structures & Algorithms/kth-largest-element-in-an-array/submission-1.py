class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heap of size k
        #return top 

        heap = []

        for n in nums:
            heapq.heappush(heap,n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

        '''
        heapq.heappop(heap)
        heapq.heappush(heap,0)

        #min heap default
        #transform in place
        heapq.heapify(nums)

        use - for max heap
        '''

      