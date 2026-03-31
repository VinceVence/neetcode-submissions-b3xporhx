class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        h = 0

        while l < r:
            if heights[l] > heights[r]:
                area = (r - l) * heights[r]
                h = max(area, h)
                r -= 1
            else:
                area = (r - l) * heights[l]
                h = max(area, h)
                l += 1
        return h
