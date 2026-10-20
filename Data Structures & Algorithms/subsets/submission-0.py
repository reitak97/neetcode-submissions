class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  

        res = []

        def dfs(i,curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            #only move forward

            #add
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()

            #don't add
            dfs(i+1,curr)



        dfs(0,[])
        return res

        #n * 2^n
        #copy each subset, 2 decisions for each index


        