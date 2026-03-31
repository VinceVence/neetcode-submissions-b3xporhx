class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl = 0
        maxr = 0
        tot = 0

        while l < r: 
            if height[l] < height[r]:
                if maxl - height[l] < 0:
                    maxl = height[l]
                else:
                    tot += (maxl - height[l])
                l += 1
            else:
                if maxr - height[r] < 0:
                    maxr = height[r]
                else:
                    tot += (maxr - height[r])
                r-=1
        return tot


        