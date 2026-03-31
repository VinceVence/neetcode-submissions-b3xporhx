class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            curr = target - nums[i]
            if curr not in d.keys():
                d[nums[i]] = i
            else:
                return [d[curr], i]
