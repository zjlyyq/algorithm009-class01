class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        target = sum_nums // 2
        if target * 2 != sum_nums:
            return False
        
        n = len(nums)
        dp = [False] * target+1
        dp[0] = True
        dp[nums[0]] = True
        # pre = []
        for i in range(1, n):
            # pre = [] + dp
            for j in range(target, nums[i]-1, -1):
            # for j in range(nums[i], target+1):
                dp[j] = dp[j] or dp[j-nums[i]]
                if dp[target]:
                    return True
        return False