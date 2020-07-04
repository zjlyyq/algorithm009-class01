class Solution:
    cache = []
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            self.cache.append(0)
        return self.dfs(nums, 0)
        
    def dfs(self, nums: List[int], pos: int) -> bool:
        if pos + nums[pos] >= len(nums)-1:
            return True
        if nums[pos] == 0: return False

        for i in range(nums[pos]):
            if self.cache[pos+i+1] == 1: return True
            elif self.cache[pos+i+1] == -1: continue 
            else:
                self.cache[pos+i+1] = self.dfs(nums, pos+i+1)
                if self.cache[pos+i+1] == 1: return True
        return False