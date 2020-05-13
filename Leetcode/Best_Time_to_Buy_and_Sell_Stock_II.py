class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        p = 1
        while p < len(prices):
            if prices[p] > prices[p - 1]:
                sum = sum + prices[p] - prices[p - 1]
            p = p + 1
        return sum
