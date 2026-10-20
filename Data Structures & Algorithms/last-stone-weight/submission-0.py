class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #O(n)
        #negate elmeents
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >=2:
            heaviest_one = heapq.heappop(stones)
            heaviest_two = heapq.heappop(stones)

            if heaviest_one != heaviest_two:
                heapq.heappush(stones,heaviest_one-heaviest_two)

        return -stones[0] if stones else 0


