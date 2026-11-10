class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        for n in range(2,len(nums)):
            nums[n] += nums[n-2]
            res = max(res,nums[n])


        return res
