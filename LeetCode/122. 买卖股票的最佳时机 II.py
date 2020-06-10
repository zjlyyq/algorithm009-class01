class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        int buyPrice = 100001
        int earning = 0
        for  price in prices:
            if price < buyPrice:
                buyPrice = price
            else:
                earning += price-buyPrice
                buyPrice = price
        return earning