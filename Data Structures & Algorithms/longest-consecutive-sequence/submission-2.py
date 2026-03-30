class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
        longest = 1
        for num in s:
            if num-1 not in s:
                length = 1
                while num+length in s:
                    length = length+1
                if longest<length:
                    longest = length
        return longest