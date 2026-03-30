class Solution:
    def trap(self, height: List[int]) -> int:
        a=[]
        sum=0
        l_m =[]
        l_l = 0
        r_l = 0
        r_m = []
        for i in range(len(height)-1,-1,-1):
            if height[i] > r_l:
                r_l = height[i]
            r_m.append(r_l)
        r_m.reverse()
        
        for i in height:
            if i>l_l:
                l_l=i
            l_m.append(l_l)
        
        print(l_m)
        print(r_m)

        for i in range(1,len(height)-1):
            s=0
            max_left= l_m[i]
            max_right=r_m[i]
            
            s = max(min(max_left,max_right) - height[i],0)
            a.append(s)
            print(i,max_left,height[i],max_right,s,a)
        for i in range(len(a)):
            sum+=a[i]
        return sum


            
            
           
            
            
            

        

        