package LeetCode;

import java.util.Stack;

/*
 * @lc app=leetcode.cn id=84 lang=java
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
class Solution {
    public int largestRectangleArea(int[] heights) {
        int ans = 0;
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(-1);
        for (int i = 0;i < heights.length;i ++) {
            while(stack.peek() != -1 && heights[stack.peek()] >= heights[i]){
                ans = Math.max(ans, heights[stack.pop()]*(i-stack.peek()-1));
            }
            stack.push(i);
        }
        while(stack.peek() != -1) {
            ans = Math.max(ans, heights[stack.pop()]*(heights.length-stack.peek()-1));
        }
        return ans;
    }
}
// @lc code=end

