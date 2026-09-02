class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset, res = set(), set()
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        for n in nums:
            numset.add(n)

        for n in numset:
            nextnum = n + 1
            if n - 1 not in numset:
                count = 1
                res.add(count)
                if nextnum in numset:
                    while nextnum in numset:
                        nextnum += 1
                        count += 1
                    res.add(count)
        return max(res)




