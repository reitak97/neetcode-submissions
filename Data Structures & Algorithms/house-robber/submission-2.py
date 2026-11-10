class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return max(nums[0],nums[1])

        res = 0
        for n in range(2,len(nums)):
            nums[n] += nums[n-2]
            res = max(res,nums[n])


        return res
