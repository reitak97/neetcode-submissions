class Solution:
    def rob(self, nums: List[int]) -> int:
        

        #either add current + nums[i-2] or use nums[i-1]
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[1],nums[0])
        res = [0] *  len(nums) 
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-1], nums[i-2]+nums[i])

        return nums[len(nums)-1]
        
        