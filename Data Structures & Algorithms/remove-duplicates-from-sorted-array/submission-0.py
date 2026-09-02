class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lp = 0
        for i in range(len(nums))[1:]:
            if nums[i] != nums[lp]:
                lp += 1
                nums[lp] = nums[i]

        return lp +1

            
