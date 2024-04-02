class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff_adj = []
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
                diff_adj.append(prices[i+1] - prices[i])
        return sum(diff_adj) 