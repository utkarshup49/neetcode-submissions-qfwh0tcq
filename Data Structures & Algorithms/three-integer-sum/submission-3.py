class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        r = []
        nums =  sorted(nums)
        for i in range(l-1):
            a = nums[i]
            left = 0
            right = l-1
            while left<right:
                print(i, left, right)
                if left == i:
                    left+=1
                    continue
                if right == i:
                    right-=1
                    continue

                total = a + nums[left] + nums[right]
    
                if total == 0:
                    if sorted([nums[i], nums[left], nums[right]]) not in r:
                        r.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return r


        
        