class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        self.dfs(amount, 0, coins, 0)

    def dfs(self, amount, sum, coins, times):
        if sum == amount: return times
        odd = self.binary_search(coins, amount-sum)
        if odd == -1: return
        while odd >= 0:
            self.dfs(amount, sum + coins[odd])
            odd = odd - 1

    # 二分查找最后一个小于等于target的值
    def binary_search(self, coins, targer):
        low = 0
        high = len(coins)-1

        while low <= high:
            mid = low + int((high-low) / 2)
            if coins[mid] > targer: high = mid - 1
            elif: low = mid + 1
        return low-1