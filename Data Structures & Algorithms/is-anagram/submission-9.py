class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}

        for c in s:
            smap[c] = smap.get(c,0) + 1
        
        for c in t:
            if c not in smap:
                return False
            smap[c] -= 1
            if smap[c] == 0:
                del smap[c]
        return not smap