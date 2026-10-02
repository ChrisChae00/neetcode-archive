class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch.lstrip('-').isdigit():
                stack.append(ch)   
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if ch == "+":
                    temp = num1 + num2
                    stack.append(temp)
                elif ch == "-":
                    temp = num1 - num2
                    stack.append(temp)
                elif ch == "*":
                    temp = num1 * num2
                    stack.append(temp)
                elif ch == "/":
                    temp = num1 / num2
                    stack.append(temp)
                
        return int(stack[-1])
