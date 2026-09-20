class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {"(": ")", "[": "]", "{": "}"}
        stack = []

        if len(s) % 2 != 0:
            return False
        
        for c in s:
            if c in bracketsMap.keys():
                stack.append(bracketsMap[c])
            else:
                if not stack or c != stack[-1]:
                    return False
                else:
                    stack.pop()
        return True if not stack else False

            
            