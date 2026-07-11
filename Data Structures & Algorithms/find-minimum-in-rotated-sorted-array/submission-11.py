class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r) // 2

            #if m in bigger sorted side
            if nums[m] > nums[r]:
                #search right
                l = m + 1

            # we are in sorted side
            else:
                r = m    
        return nums[l]
        