class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = post = 1
        output = [1 for _ in range(len(nums))]
        tot = 0

        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output
        