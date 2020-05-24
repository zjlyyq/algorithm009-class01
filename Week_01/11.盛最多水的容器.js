/*
 * @lc app=leetcode.cn id=11 lang=javascript
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let i = 0, j = height.length - 1;
    let ans = 0;
    while(i < j) {
        ans = max( ans, (j-i) * min(height[i], height[j]) );
        if (height[i] > height[j]) {
            j --;
        }
        else {
            i ++;
        }
        
    }
    return ans;
};

function min(a, b) {
    return a < b?a:b;
}

function max(a, b) {
    return a > b?a:b;
}
// @lc code=end

