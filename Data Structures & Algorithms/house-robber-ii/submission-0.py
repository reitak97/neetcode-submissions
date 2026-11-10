class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        #exclude first
        res = [0] * (len(nums)-1)
        res[0] = nums[1]
        res[1] = max(nums[1],nums[2])

        for i in range(2,len(nums)-1):
            res[i] = max(res[i-2] + nums[i+1], res[i-1])
        
        exFirst = res[len(nums)-2]



        #exclude last
        res1 = [0] * (len(nums)-1)
        res1[0] = nums[0]
        res1[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            res1[i] = max(res1[i-2] + nums[i], res1[i-1])

        exLast = res1[len(nums)-2]



        return max(exFirst,exLast)