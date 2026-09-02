class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
            if n - 1 not in numset:
                count = 1
                nextnum = n + 1

                while nextnum in numset:
                    count += 1
                    nextnum += 1
                
                if count > longest:
                    longest = count
        return longest
