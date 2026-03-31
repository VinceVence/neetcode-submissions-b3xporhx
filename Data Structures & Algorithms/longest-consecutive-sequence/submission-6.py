class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 in numset:
                continue
            k = 0
            while nums[i] + k in numset:
                k += 1
            longest = max(longest, k)
        return longest

