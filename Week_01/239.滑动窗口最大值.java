package LeetCode;

import java.util.Deque;
import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=239 lang=java
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
class Solution2 {

    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> deque = new LinkedList<Integer>();
        int[] ans = new int[nums.length-k+1];
        for(int i = 0;i < nums.length;i ++) {
            if (deque.isEmpty()) {
                deque.add(i);
                if (i >= k-1) {
                    ans[i-k+1] = nums[deque.getFirst()];
                }
                continue;
            }
            while (nums[deque.getLast()] < nums[i]){
                deque.removeLast();
                if (deque.isEmpty()) {
                    break;
                }
            }
            deque.add(i);
            while (deque.getFirst() <= (i-k)) {
                deque.removeFirst();
                if (deque.isEmpty()) {
                    break;
                }
            }
            if (i >= k-1) {
                ans[i-k+1] = nums[deque.getFirst()];
            }
        }
        return ans;
    }
}
// @lc code=end

