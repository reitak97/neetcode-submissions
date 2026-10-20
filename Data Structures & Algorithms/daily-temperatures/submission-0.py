class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonically decreasing stack
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                cur = stack.pop()
                res[cur[1]] = i - cur[1]

            stack.append((t,i))

        
        return res