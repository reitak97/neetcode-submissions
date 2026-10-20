class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return


            #include
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()


            #dont include
            dfs(i+1)


        dfs(0)
        return res