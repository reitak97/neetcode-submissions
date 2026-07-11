class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = []
        for i in nums:
            if i not in s:
                s.append(i)
            else:
                return True
        return False