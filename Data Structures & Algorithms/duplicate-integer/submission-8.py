class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        DupMap = {}
        for n in nums:
            if n in DupMap:
                return bool(DupMap)
            DupMap.setdefault(n, 0)
        return False
        
