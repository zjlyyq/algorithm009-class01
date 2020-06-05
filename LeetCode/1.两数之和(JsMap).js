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
    map = new Map();
    for(let i = 0;i < nums.length;i ++){
        if (map.get(nums[i])) {
            map.get(nums[i]).push(i);
        }else {
            map.set(nums[i],[i]);
        } 
    }
    for (let i of nums) {
        if (map.get(target-i) && target == i*2) {
            if ((map.get(target-i)).length >= 2){
                return [(map.get(target-i))[0], (map.get(target-i))[1]];
            }
        }
        if (map.get(target-i) && target != i*2){
            return [(map.get(i))[0], (map.get(target-i))[0]];
        }
    }
    return 0
};
// @lc code=end

