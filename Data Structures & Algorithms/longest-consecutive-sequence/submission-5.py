class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        maxnum = 0
        

        for i in range(len(nums)):
            if nums[i] - 1 in ns:
                continue
            l = 0
            
            while nums[i] + l in ns:
                l += 1
            maxnum = max(l, maxnum)
        return maxnum