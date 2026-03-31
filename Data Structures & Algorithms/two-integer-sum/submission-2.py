class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            if target - num not in hm.keys():
                hm[num] = i
            else: 
                return [hm[target-num], i]
                    
        