class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr =[]
        seen = set()
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for n in nums:
                if n not in seen:
                    curr.append(n)
                    seen.add(n)
                    dfs()
                    curr.pop()
                    seen.remove(n)



        dfs()
        return res