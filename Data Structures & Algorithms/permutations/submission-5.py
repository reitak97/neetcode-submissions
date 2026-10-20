class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        seen = [False] * (len(nums))
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(0,len(nums)):
                if not seen[j]:
                    curr.append(nums[j])
                    seen[j] = True
                    dfs()
                    curr.pop()
                    seen[j] = False
                    




        dfs()

        return res

