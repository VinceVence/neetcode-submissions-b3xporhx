class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        length = 0

        for n in nums:
            if n - 1 not in numset:
                longest = 0
                while (n + longest) in numset:
                    longest += 1
                length = max(length, longest)
        return length
        