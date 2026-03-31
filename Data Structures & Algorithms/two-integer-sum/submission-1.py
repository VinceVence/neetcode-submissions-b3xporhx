class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if (a + b == target) & (i != j):
                    return [i, j]
                    
        