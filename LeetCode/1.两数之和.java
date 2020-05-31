import java.util.HashMap;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=1 lang=java
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        int [] ans = new int[2];
        for(int i = 0;i < nums.length;i ++) {
            if (map.get(target-nums[i]) != null) {
                ans[0] = i;
                ans[1] = map.get(target-nums[i]);
                break;
            }
            map.put(nums[i], i);
        }
        for(int i = 0;i < nums.length;i ++) {
            if (map.get(target-nums[i]) != null && map.get(target-nums[i])!=i) {
                ans[0] = i;
                ans[1] = map.get(target-nums[i]);
                break;
            }
        }
        return ans;
    }
}
// @lc code=end

