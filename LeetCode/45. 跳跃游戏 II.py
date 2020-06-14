class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        queue = []
        queue.append(0)
        while queue:
            cur = queue.pop(0)
            if cur + nums[i] > len[nums]-1:
                return ans
            next = -1
            Max = -1
            for i in range(nums[cur]+1):
                if i + nums[cur+i] > Max:
                    Max = i + nums[cur+i]
                    next = cur + i
            queue.append(next)
        return ans