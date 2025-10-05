class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        profit, hold = 0, -inf

        for price in prices:
            profit = max(profit, hold + price - fee)
            hold = max(hold, profit - price)
        
        return profit