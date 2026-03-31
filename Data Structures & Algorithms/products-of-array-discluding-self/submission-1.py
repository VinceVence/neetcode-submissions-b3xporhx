class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]
        pre = 1
        post = 1

        for i in range(len(nums)):
            if i == 0:
                out[i] = 1
                pre = pre * nums[i]
                continue
            
            out[i] = pre
            pre = pre * nums[i]
        print(out)

        for i in range(len(nums) -1, -1, -1):
            out[i] = out[i] * post
            post = post * nums[i]

        return out
            
        