class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = math.inf
        max_profit = 0
        for i in prices:
            low_price = min(i,low_price)
            max_profit = max(max_profit, i-low_price)
        return max_profit
