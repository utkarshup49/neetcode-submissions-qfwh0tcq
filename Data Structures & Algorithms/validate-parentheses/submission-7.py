class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(',']':'[','}':'{'}
        print(dic)
        print(dic[')'])

        for i in s:
            if i in dic:
                if not stack or stack[-1] != dic[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack) == 0

        