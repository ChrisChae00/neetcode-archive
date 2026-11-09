class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for ch in s:
            sMap[ch] = sMap.get(ch,0) + 1
        
        for c in t:
            if c in sMap:
                sMap[c] -= 1
                if sMap[c] == 0:
                    del sMap[c]
            else:
                return False
        return not bool(sMap)
