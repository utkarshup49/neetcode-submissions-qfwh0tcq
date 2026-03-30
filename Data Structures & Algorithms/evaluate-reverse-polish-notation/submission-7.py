class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            print(stack)
            if i == "+":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a+b)
            elif i == "-":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b-a)
            elif i == "*":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(a*b)
            elif i == "/":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(b/a)
            else:
                stack.append(i)
        print(stack)
        a = int(stack[0])
        return a   