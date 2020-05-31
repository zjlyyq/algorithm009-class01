/*
 * @lc app=leetcode.cn id=198 lang=java
 *
 * [198] 打家劫舍
 */

// @lc code=start
class Solution {
    public int rob(int[] nums) {
        int [][] dp = new int [2][2];
        int maxSum = 0;
        for (int i = 1;i <= nums.length;i ++) {
            dp[i%2][0] = Math.max(dp[(i-1)%2][0], dp[(i-1)%2][1]);
            dp[i%2][1] = dp[(i-1)%2][0] + nums[i-1];
        }
        return Math.max(dp[(nums.length)%2][0], dp[(nums.length)%2][1]);
    }
}
// @lc code=end

