class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, -1, -1):
            for m in freq[i]:
                output.append(m)
                if len(output) == k:
                    return output
        return []

        