class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,total,curr):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return

            #include this num 
            curr.append(nums[i])
            dfs(i,total+nums[i],curr)
            curr.pop()
            #pop since we are sharing array state

            dfs(i+1,total,curr)
            #skip



        dfs(0,0,[])
        return res
