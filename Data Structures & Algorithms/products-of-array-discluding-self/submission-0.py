class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for i in range(len(nums) - 1)]
        pre = 1
        post = 1

        for i in range(len(nums)):
            
            if i == 0:
                out.append(1)
    
            out[i] = out[i-1] * pre
            pre = nums[i] 
        print(out)

        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * post
            post = post * nums[i]

        return out

