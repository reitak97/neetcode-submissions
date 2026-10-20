class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        rightMax = 0 
        l = 0
        r = len(height)-1
        res = 0 
        while l < r:
            if height[l] < height[r]:
                leftMax = max(height[l],leftMax)
                res += leftMax - height[l]
                
                l +=1

            else:
                rightMax = max(height[r],rightMax)

                res += rightMax - height[r]
                r-=1


        return res