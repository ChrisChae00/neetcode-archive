class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {")": "(", "}": "{",  "]":"["}
        stack = []

        for c in s:
            if c in bracketsMap:
                if stack and stack[-1] == bracketsMap[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        return True if not stack else False