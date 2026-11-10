class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        #extend previous sum or starting fresh with current

        cur = 0 
        for n in nums:
            if n + cur >0:
                cur += n
                res = max(res,cur)

            else:
                cur = 0


            


        return res