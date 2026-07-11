class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])

        res = nums
        res[1] = max(res[0],res[1])
        for i in range(2,len(nums)):
            res[i] = max(res[i-1], res[i-2]+ res[i])

        return res[len(nums)-1]