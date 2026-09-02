class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            temp = target - n 

            if temp in hashmap:
                return [hashmap[temp], i]

            hashmap[n] = i
