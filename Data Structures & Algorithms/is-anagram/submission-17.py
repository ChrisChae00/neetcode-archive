class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tMap = {}
        if not len(s) == len(t): return False

        for c in t:
            tMap[c] = tMap.get(c,0) +1

        for c in s:
            if c not in tMap:
                return False
            else:
                tMap[c] -= 1
                if tMap[c] == 0:
                    del tMap[c]
        return not bool(tMap)
            