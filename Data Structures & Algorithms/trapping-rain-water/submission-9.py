class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = 0
        maxR = 0
        res = 0

        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                if height[l] > maxL:
                    maxL = height[l]
                else:
                    res += maxL - height[l]
                l += 1
            else:
                if height[r] > maxR:
                    maxR = height[r]
                else:
                    res += maxR - height[r]
                r -= 1
        return res
                    



        