class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = [] # i, h

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ind, height = stack.pop()
                maxA = max(maxA, height * (i - ind))
                start = ind
            stack.append((start, h))


        for i, h in stack:
            maxA = max(maxA, (len(heights) - i) * h)
        return maxA
        