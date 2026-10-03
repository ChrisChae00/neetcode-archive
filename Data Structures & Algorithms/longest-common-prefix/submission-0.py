class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        prefix = ""

        for i,ch in enumerate(temp):
            checker = 0
            for word in strs[1:]:
                if i < len(word) and temp[i] == word[i]:
                    checker += 1
                else:
                    return prefix
            if checker == len(strs) - 1:
                prefix += ch
        return prefix if prefix else ""

