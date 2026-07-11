class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r) //2
            if nums[m] == target:
                return m
            #if we are in left sorted portion
            elif nums[m] >= nums[l]:
                #target is between left and mid
                if nums[l] <= target <= nums[m]:
                    r = m -1
                else:
                    l = m + 1

            #if we are in right sorted portion
            else:
                #if target between mid and right
                if nums[m] <= target <= nums[r]:
                    l = m +1
                else:
                    r = m -1







        return -1
        