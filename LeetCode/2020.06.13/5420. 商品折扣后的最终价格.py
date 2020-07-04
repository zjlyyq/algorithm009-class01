class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        p_size = len(prices)
        ans = [0] * p_size
        
        for i in range(p_size):
            while stack and prices[stack[-1]] >= prices[i]:
                ans[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
                
            stack.append(i)
        while stack:
            ans[stack[-1]] = prices[stack.pop()]
        return ans
