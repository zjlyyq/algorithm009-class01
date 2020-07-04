class Solution:
    maxWeight = 0
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        # 递归求解0-1背包
        def dfs(level, weight):
            if level == n or weight == target:
                if weight > self.maxWeight:
                    self.maxWeight = weight
                return
            if cache[level][weight]:
                return
            cache[level][weight] = True
            dfs(level + 1, weight)
            if weight + nums[level] <= target:
                dfs(level + 1, weight+nums[level])
                
        sum_nums = sum(nums)
        target = sum_nums // 2
        if target * 2 != sum_nums:
            return False
        cache = [[False]*(target+1) for i in range(len(nums))]
        dfs(0, 0)
        if self.maxWeight == target:
            return True
        else: 
            return False
        