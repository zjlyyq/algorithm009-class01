class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        target = sum_nums // 2
        if target * 2 != sum_nums:
            return False
        n = len(nums)
        dp = [[False]*(target+1) for i in range(2)]
        dp[0][0] = True
        if nums[0] < target + 1:
            dp[0][nums[0]] = True
        for i in range(1,n):
            for j in range(target+1):
                if j >= nums[i]:
                    dp[i%2][j] = dp[(i-1)%2][j] or dp[(i-1)%2][j-nums[i]]
                else:
                    dp[i%2][j] = dp[(i-1)%2][j]
        return dp[-1][-1]