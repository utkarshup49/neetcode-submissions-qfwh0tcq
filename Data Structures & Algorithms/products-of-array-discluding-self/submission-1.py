class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = size * [1]
        prefix = 1
        postfix = 1
       
        for i in range(size):
            output[i] = prefix
            prefix = prefix * nums[i]
        for i in range(size-1,-1,-1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]
        return output
        
