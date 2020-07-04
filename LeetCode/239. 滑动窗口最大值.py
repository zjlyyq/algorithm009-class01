from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def clear_deque(pos):
            # 判断队列头部是否该出队了
            if dq and (dq[0]+k) == pos:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[pos]:
                dq.pop()

        dq = deque()
        ans = []
        n = len(nums)
        maxpos = 0
        for i in range(k):
            clear_deque(i)
            dq.append(i)
            if nums[i] > nums[maxpos]:
                maxpos = i
        ans.append(nums[maxpos])

        for i in range(k, n):
            clear_deque(i)
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans