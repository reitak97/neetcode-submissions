class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonically decreasing stack
        res = [0] * len(temperatures)

        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prev, _ = stack.pop()
                res[prev] = i - prev


            stack.append((i,t))
        return res


   