class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            left = i
            right = i+1
            count=1
            while right<=len(temperatures)-1:
                print(left,right)
                if temperatures[left] >= temperatures[right]:
                    right+=1
                    count+=1
                else:
                    arr[i] = count
                    break
        return arr
