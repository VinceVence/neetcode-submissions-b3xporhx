class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            if target - num not in d.keys():
                d[num] = i
            else:
                return [d[target-num], i]
        