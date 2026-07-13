class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False

        #[1,2,3,3]
        #seen = (1,2,3)
        #[]