class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(',']':'[','}':'{'}
        

        for i in s:
            if i in dic:
                if not stack or stack[-1] != dic[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        if stack:
            return False
        else:
            return True

        