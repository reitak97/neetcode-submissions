class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #[-4,-1,-1,0,1,2]
        for i in range(len(nums)-2):
            
            #skip duplicates
            if nums[i] == nums[i-1] and i >0:
                continue

            l = i +1
            r  = len(nums)- 1
            while l < r:
                currSum = nums[i] + nums[r] + nums[l]

                if currSum < 0:
                    l +=1
                elif currSum > 0:
                    r-=1
                else:
                    res.append([nums[i],nums[r],nums[l]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1

        return res
           
