class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newNums = nums.sort()
        res = []
        #[-4,-1,-1,0,1,2]\
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                if n + nums[l] + nums[r] > 0:
                    r -=1
                elif  n + nums[l] + nums[r] < 0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                 
                    l+=1
                    while nums[l]== nums[l-1] and l <r:
                        l+=1
                    
                    
        
        return res
            

        