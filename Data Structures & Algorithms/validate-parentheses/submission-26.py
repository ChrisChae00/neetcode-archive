class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"(": ")", "[": "]", "{": "}"}
        stack = []
        
        for c in s:
            if c in hashmap.values():
                if stack and c == stack[-1]: stack.pop()
                else: return False
            else: stack.append(hashmap[c])
        return True if not stack else False