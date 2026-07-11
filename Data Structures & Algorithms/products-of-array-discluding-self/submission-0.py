class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        newList = []

        for i in range(len(nums)):
            lastNum = nums.pop(0)
            total = 1
            for n in nums:
                total *= n 
            newList.append(total)
            nums.append(lastNum)
        return newList