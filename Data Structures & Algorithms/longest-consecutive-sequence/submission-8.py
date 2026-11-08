class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest = 0
        
        for n in nums:
            if (n-1) not in hs:
                length = 0
                i = 0
                while n + i in hs:
                    length += 1 
                    i += 1
                longest = max(longest, length)
        return longest
            
            

        