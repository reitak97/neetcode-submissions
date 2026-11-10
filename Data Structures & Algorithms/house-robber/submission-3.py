class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return nums[1]

        res = 0 
        for i in range(2,len(nums)):
            nums[i] = nums[i] + nums[i-2]
            res = max(res,nums[i])


        return res