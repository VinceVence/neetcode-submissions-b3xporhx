class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        res = 0

        for i in range(len(nums)):
            l = 0
            while nums[i] - l in ns:
                l += 1
            res = max(res, l)
        return res
            
