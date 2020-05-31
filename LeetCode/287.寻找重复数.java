/*
 * @lc app=leetcode.cn id=287 lang=java
 *
 * [287] 寻找重复数
 */

// @lc code=start
class Solution {
    public int findDuplicate(int[] nums) {
        int l = 0, r = nums.length - 1;
        int mid;
        while(l < r) {
            mid = (l + r) >> 1;
            int cnt = 0;
            for (int i = 0;i < nums.length;i ++) {
                if (nums[i] < mid) {
                    cnt ++;
                }
            }
            if (cnt <= mid) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }
        return mid;
    }
}
// @lc code=end

