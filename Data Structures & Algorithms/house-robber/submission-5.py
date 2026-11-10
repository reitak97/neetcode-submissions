class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        res = 0
        for i in range(len(nums)):
            if i > 1:
                nums[i] += nums[i-2]
            res = max(res,nums[i])
        return res