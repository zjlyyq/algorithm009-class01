/*
 * @lc app=leetcode.cn id=1 lang=javascript
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    map = {}
    for(let i = 0;i < nums.length;i ++){
        if (map[nums[i]]) {
            map[nums[i]].push(i);
        }else {
            map[nums[i]] = [i];
        } 
    }
    for (let i of nums) {
        if (map[target-i] && target == i*2) {
            if (map[i].length >= 2){
                return [map[i][0], map[i][1]];
            }
        }
        if (map[target-i] && target != i*2){
            return [map[i][0], map[target-i][0]];
        }
    }
    return 0
};
// @lc code=end

