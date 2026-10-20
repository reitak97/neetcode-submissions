class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for n in nums:
            #start of seq
            if n-1 not in store:
                curr = 0
                while n in store:
                    curr += 1
                    n +=1
                res = max(res,curr)

        return res



