#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum = 0;
        for i in nums:
            sum = sum + i;
        if sum%k != 0:
            return False
        for len in range(k-3):
        return True
        
# @lc code=end

