class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0

        while l < len(nums) - k + 1:
            print(nums[l: l + k])
            res.append(max(nums[l: l + k]))
            l += 1
        print(res)
        return res
        