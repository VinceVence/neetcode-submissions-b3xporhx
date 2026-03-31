class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxnum = 0

        for i in range(len(nums)):
            if nums[i] - 1 in numset:
                continue
            
            m = 0
            longest = 0
            while nums[i] + m in numset:
                longest += 1
                m +=1
            maxnum = max(maxnum, longest)
        return maxnum
            
        