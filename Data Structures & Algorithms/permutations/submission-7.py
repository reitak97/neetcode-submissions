class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = [False] * len(nums)

        res = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())

            for i,p in enumerate(nums):
                if not seen[i]:
                    seen[i] = True
                    curr.append(p)
                    dfs(curr)
                    curr.pop()
                    seen[i] = False





        dfs([])
        return res