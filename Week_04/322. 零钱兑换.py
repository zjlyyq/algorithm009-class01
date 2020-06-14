class Solution:
    ans = 1 << 31
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        print(coins)
        return self.dfs(amount, 0, coins, 0)

    def dfs(self, amount, sum, coins, times):
        if sum == amount: 
            return times
        odd = self.binary_search(coins, amount-sum)
        if odd == -1: return -1
        while odd >= 0:
            k = int((amount-sum)/coins[odd])
            for i in range(k):
                j = k - i
                ret = self.dfs(amount, sum + j*coins[odd], coins, times+j)
                if ret != -1:
                    return ret
            odd = odd - 1
        return -1

    # 二分查找最后一个小于等于target的值
    def binary_search(self, coins, targer):
        # print('target:'+str(targer))
        low = 0
        high = len(coins)-1
        while low <= high:
            mid = low + int((high-low) / 2)
            if coins[mid] > targer: high = mid - 1
            else: low = mid + 1
        # print(low-1)
        return low-1