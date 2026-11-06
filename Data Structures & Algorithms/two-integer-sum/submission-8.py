class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            t = target - nums[i]
            if t in h.keys():
                return [h[t], i]
            else:
                h[nums[i]] = i
        return [h[t], i]