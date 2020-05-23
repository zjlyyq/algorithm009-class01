package LeetCode;

/*
 * @lc app=leetcode.cn id=84 lang=java
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
class Solution {
    public int largestRectangleArea(int[] heights) {
        if(heights.length == 0) {
            return 0;
        }
        int ans = heights[0];
        int l = heights.length;
        int h1,h2;
        for(int i = 0;i < l;i ++) {
            h1 = heights[i];
            if (h1 > ans) ans = h1;
            for(int j = i+1;j < l;j ++){
                h2 = heights[j] < h1?heights[j]:h1;
                h1 = h2;
                if (h2*(j-i+1) > ans) ans = h2*(j-i+1);
            }
        }
        return ans;
    }
}
// @lc code=end

