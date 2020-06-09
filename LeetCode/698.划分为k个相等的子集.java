import java.sql.Array;
import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=698 lang=java
 *
 * [698] 划分为k个相等的子集
 */

// @lc code=start
class Solution {
    public int comparetor(int a, int b){
        if (a > b) return 1;
        else if (a < b) return -1;
        else return 0;
    }
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for(int i : nums) {
            sum += i;
        }
        Arrays.sort(nums);
        System.out.printf(Arrays.toString(nums));
        if (sum%k != 0) return false;
        for(int len = 1;len <= nums.length-3; len ++){
            
        }
        return true;
    }    
}
// @lc code=end

