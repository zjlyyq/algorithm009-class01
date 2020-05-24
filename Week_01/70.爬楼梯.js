/*
 * @lc app=leetcode.cn id=70 lang=javascript
 *
 * [70] 爬楼梯
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let last1 = 1;
    let last2 = 1;
    ans = 1;
    for (let i = 2;i <= n;i ++) {
        ans = last1 + last2;
        let t = last1;
        last2 = last1;
        last1 = ans;
    }
    return ans;
};
// @lc code=end

