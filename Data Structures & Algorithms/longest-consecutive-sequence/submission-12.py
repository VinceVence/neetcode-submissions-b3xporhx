class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in ns:
                i = 0
                while n + i in ns:
                    i += 1
                longest = max(i, longest)
        return longest
        