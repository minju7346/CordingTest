class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        profit = 0
        i = 0
        j = 1
        while j < size:
            if prices[i] < prices[j]:
                profit += prices[j] - prices[i]
            i = j
            j = i + 1
        return profit
