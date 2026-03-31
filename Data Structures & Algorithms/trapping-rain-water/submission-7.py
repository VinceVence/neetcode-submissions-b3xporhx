class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxL, maxR = 0, 0
        l = 0
        r = len(height) - 1

        while l < r:
            if height[r] > height[l]:
                # update left
                if maxL < height[l]:
                    maxL = height[l]
                else:
                    res += (maxL - height[l])
                l += 1
            else:
                # update right
                if maxR < height[r]:
                    maxR = height[r]
                else:
                    res += (maxR - height[r])
                r -= 1
        return res
        