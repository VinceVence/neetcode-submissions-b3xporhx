class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_out = 0
        r_out = len(matrix) - 1
        while l_out <= r_out:
            mat_out = (l_out + r_out) // 2
            nums = matrix[mat_out]
            if nums[0] <= target and nums[-1] >= target:
                l = 0
                r = len(nums) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] > target:
                        r = mid - 1
                    elif nums[mid] < target:
                        l = mid + 1
                    else:
                        return True
                return False
            elif nums[-1] < target:
                l_out = mat_out + 1
            elif nums[0] > target:
                r_out = mat_out - 1
        return False
                    
                    

