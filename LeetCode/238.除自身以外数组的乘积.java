import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=238 lang=java
 *
 * [238] 除自身以外数组的乘积
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size = nums.length;
        int [] pre = new int[size];
        int [] sub = new int[size];
        int [] ans = new int[size];
        pre[0] = 1;
        for (int i = 0;i < size-1 ;i ++) pre[i+1] = pre[i]*nums[i];
        sub[size-1] = 1;
        for (int j = size-1;j > 0 ;j --) sub[j-1] = sub[j]*nums[j]; 
        for (int i = 0;i < size;i ++) {
            ans[i] = pre[i]*sub[i];
        }
        return ans;
    }
}
// @lc code=end

