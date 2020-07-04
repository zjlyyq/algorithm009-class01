class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = []
        ans.append(1<<31)
        visited = [1<<31]*2*len(nums)
        self.dfs(nums, 0, ans, visited, 0)
        return ans[0]
    def dfs(self, nums, cur, ans, visited, times):
        visited[cur] = min(visited[cur], times)
        if cur >= len(nums) - 1:
            ans[0] = min(times, ans[0])
            return
        k = nums[cur]
        for i in range(k): 
            if cur + k - i > len(nums)-1: 
                continue
            if (times + 1) < visited[cur + k - i] and (times + 1) < ans[0]:
                self.dfs(nums, cur + k - i, ans, visited, times + 1)