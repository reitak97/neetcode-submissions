class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []
        curr = []
        def dfs():
            #base
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(len(nums)):
                if not used[j]:
                    used[j] = True
                    curr.append(nums[j])
                    dfs()
                    curr.pop()
                    used[j] = False


            

        dfs()
        return res