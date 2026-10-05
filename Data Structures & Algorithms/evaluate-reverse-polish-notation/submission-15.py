class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))   
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if ch == "+":
                    stack.append(num1 + num2)
                elif ch == "-":
                    stack.append(num1 - num2)
                elif ch == "*":
                    stack.append(num1 * num2)
                elif ch == "/":
                    stack.append(int(num1 / num2))
                
        return stack[-1]
