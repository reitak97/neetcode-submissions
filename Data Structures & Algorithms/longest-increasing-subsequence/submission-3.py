class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
    
        #each char is length 1
        dp = [1] * len(nums)
        #iterate backwards
        for i in range(len(nums)-1,-1,-1):

            #iterate forwards

            for j in range(i+1,len(nums)):
                #if current is less than next element, update dp
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)


        return max(dp)