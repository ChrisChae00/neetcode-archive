class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[lp - 1]:
                nums[lp] = nums[i]
                lp += 1

        return lp