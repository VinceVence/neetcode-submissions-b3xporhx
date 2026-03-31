class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 ,len(height) - 1
        maxL, maxR = 0, 0
        tot = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > maxL:
                    maxL = height[l]
                else:
                    tot += (maxL - height[l])
                l += 1
            else:
                if height[r] > maxR:
                    maxR = height[r]
                else:
                    tot += (maxR - height[r])
                r -= 1

        return tot

        