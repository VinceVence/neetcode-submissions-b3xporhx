class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = 0

        for r in range(len(prices)):
            if prices[l] >= prices[r]:
                l = r
            p = max(p, prices[r] - prices[l])
        return p
        