class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        output = []
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)

        for n, i in countMap.items():
            freq[i].append(n)

        for j in range(len(freq) - 1, 0, -1):
            for n in freq[j]:
                output.append(n)
                if len(output) == k:
                    return output