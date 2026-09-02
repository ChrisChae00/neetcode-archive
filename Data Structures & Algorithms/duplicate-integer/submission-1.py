class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkmap = set()

        for n in nums:
            if n in checkmap:
                return True
            checkmap.add(n)

        return False