'''
思路一：
暴力枚举：
1. 先对数组升序排序
2. 枚举三数之和，大于target直接break（由于是升序，越往后越大不用判断了）
3. 在上述过程中记录下和target最接近的三数和
'''
import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        nearvalue = 1 << 31 - 1
        ans = 0
        if nums[0] + nums[1] + nums[2] > target:
            return nums[0] + nums[1] + nums[2]
        if nums[n-1] + nums[n-2] + nums[n-3] < target:
            return nums[n-1] + nums[n-2] + nums[n-3]
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n): 
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s - target) < nearvalue:
                        nearvalue = abs(s - target)
                        ans = s
                    if  s > target:
                        break
        return ans