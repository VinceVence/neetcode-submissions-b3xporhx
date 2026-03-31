class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        tot = 0
        maxL, maxR = 0, 0

        while l < r:
            if height[l] < height[r]:
                if maxL < height[l]:
                    maxL = height[l]
                else:
                    tot = tot + (maxL - height[l])
                l+=1
            else:
                if maxR < height[r]:
                    maxR = height[r]
                else:
                    tot = tot + (maxR - height[r])
                r-=1
        return tot

        