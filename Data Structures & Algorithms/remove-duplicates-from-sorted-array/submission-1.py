class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 1
        for i in range(len(nums))[1:]:
            if nums[i] != nums[lp - 1]:
                nums[lp] = nums[i]
                lp += 1

        return lp

            
