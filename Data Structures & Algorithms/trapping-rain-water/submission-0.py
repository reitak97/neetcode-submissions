class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        res= 0
        r = len(height)-1

        rMax = 0
        lMax = 0
        while l < r:
            currL = height[l]
            currR = height[r]
            #update max
            rMax = max(rMax,currR)
            lMax = max(currL,lMax)

            if lMax < rMax:
                res += lMax - currL 
                l +=1
            
            else:
                res += rMax - currR
                r -=1

        return res
        
