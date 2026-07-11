class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = [[] for _ in range(len(nums) +1)]

        for n in nums:
            freq[n] = 1 + freq.get(n,0)

        for key,val in freq.items():
            res[val].append(key)

        a = []
        for i in range(len(res)-1,0,-1):
            for n in res[i]:
                a.append(n)
                if k == len(a):
                    return a


