class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    prod = prod*nums[j]
            output.append(prod)
            prod = 1
        return output




        