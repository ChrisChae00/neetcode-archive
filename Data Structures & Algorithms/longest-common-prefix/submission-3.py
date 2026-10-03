class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fword = strs[0]
        prefix = ""

        for i,c in enumerate(fword):
            for word in strs:
                if i > len(word) -1  or word[i] != fword[i]:
                    return prefix
            prefix += c
        return prefix