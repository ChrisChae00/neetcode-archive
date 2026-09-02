class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_nums = Counter(nums).most_common(k)
        res = []
        if k == 1:
            res.append(most_nums[0][0])
        else:
            for i in range(k):
                res.append(most_nums[i][0])
        return res