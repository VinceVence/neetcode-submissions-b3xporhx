class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = 0
        maxR = 0 
        total = 0


        while l < r:
            if height[l] < height[r]:
                if maxL < height[l]:
                    maxL = height[l]
                else:
                    total = total + (maxL - height[l])
                l += 1
            else:
                if maxR < height[r]:
                    maxR = height[r]
                else:
                    total = total + (maxR - height[r])
                r -=1
        return total