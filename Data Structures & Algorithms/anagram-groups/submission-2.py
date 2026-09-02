class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams
        for s in strs:
            key = tuple(sorted(s))
            res[key].append(s)
        return list(res.values())