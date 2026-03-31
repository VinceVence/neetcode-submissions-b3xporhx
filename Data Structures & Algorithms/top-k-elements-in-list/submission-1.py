class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # print(count)
        for n, c in count.items():
            freq[c].append(n)
        # print(freq)

        res = []
        for f in range(len(freq), 0, -1):
            for m in freq[f - 1]:
                res.append(m)
                if len(res) == k:
                    return res
