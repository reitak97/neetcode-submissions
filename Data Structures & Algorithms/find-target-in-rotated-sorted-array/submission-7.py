class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r) //2
            if nums[m] == target:
                return m
            #if we are in left sorted portion
            if nums[l] <= nums[m]:
                if nums[l] > target or target > nums[m]:
                    l = m + 1
                else:
                    r = m -1

            #if we are in right sorted portion
            else:
                if target > nums[m]:
                    l = m +1
                else:
                    r = m - 1





        return -1
        