class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        prefix = ""
        
        for i, c in enumerate(strs[0]):
            for word in strs:
                if word[i] != c:
                    return prefix
            prefix += c
        return prefix