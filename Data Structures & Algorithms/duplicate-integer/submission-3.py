class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        camp = set()

        for n in nums:
            if n in camp:
                return True
            camp.add(n)
        return False