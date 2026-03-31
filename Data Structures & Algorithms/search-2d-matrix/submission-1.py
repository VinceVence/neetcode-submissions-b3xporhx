class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_out = 0
        r_out = len(matrix) - 1

        while l_out <= r_out:
            midrow = (l_out + r_out) // 2
            if matrix[midrow][-1] >= target and matrix[midrow][0] <= target:
                l = 0 
                r = len(matrix[midrow]) - 1
                nums = matrix[midrow]
                while l <= r:
                    m = (l + r) // 2
                    if nums[m] > target:
                        r = m - 1
                    elif nums[m] < target:
                        l = m + 1
                    else: return True
                return False
            elif matrix[midrow][-1] < target:
                l_out = midrow + 1
            else:
                r_out = midrow - 1
        return False