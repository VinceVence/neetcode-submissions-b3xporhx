class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num not in d.keys():
                d[num] = 0
            else:
                return True
        return False
        