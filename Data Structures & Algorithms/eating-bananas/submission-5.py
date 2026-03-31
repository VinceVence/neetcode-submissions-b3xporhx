class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        res = r

        while l <= r:
            k = (r + l) // 2
            c = 0

            for p in piles:
                c += math.ceil(p / k)

            if c <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
