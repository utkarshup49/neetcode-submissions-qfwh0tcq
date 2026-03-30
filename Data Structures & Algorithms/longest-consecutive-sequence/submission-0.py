class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        count = 0
        for i in range(len(nums)):
            e = nums[i]
            c = 1
            for j in range(len(nums)):
                
                if nums[j] == e+1:
                    c = c+1
                    e = e+1
                if c>count:
                    count = c
        return count       

                
                    

        




        