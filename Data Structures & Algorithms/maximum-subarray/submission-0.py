class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            
            #extend with previous if total increases
            if nums[i]+ res > 0:
                res += nums[i]

            #starting new subarray
            else:
                #reset res
                res = 0
        return res
            
