class Solution:
    def trap(self, height: List[int]) -> int:
        a=[]
        sum=0
        for i in range(1,len(height)-1):
            s=0
            max_left=0
            max_right=0
            for j in range(0,i):
                if height[j]>max_left:
                    max_left = height[j]
            for j in range(i+1,len(height)):
                if height[j]>max_right:
                    max_right = height[j]
            s = max(min(max_left,max_right) - height[i],0)
            a.append(s)
            print(i,max_left,height[i],max_right,s,a)
        for i in range(len(a)):
            sum+=a[i]
        return sum


            
            
           
            
            
            

        

        