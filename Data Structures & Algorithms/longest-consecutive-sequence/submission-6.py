class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        #The elements do not have to be consecutive in the original array.
        #means not sliding window
        seen = set(nums)


        res = 0
        #if n-1 not in seen, start of new sequence

        for n in nums:
            if (n-1) not in seen:
                curr = 1
                while (n+1) in seen:
                    curr += 1
                    n = n + 1

                res = max(res,curr)


        return res
                