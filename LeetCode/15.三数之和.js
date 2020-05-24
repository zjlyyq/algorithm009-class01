/*
 * @lc app=leetcode.cn id=15 lang=javascript
 *
 * [15] 三数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    // 先对数组排序
    let array = nums;
    nums.sort(compare);
    if (nums.length < 3) {
        return [];
    }
    if (nums[0] == nums[nums.length-1] && nums[0]== 0) {
        return [[0,0,0]];
    }
    // console.log(nums);
    ans = [];
    map = {};
    for(let k = 0;k < nums.length-2; k ++) {
        for (let i = k + 1, j = nums.length - 1; i < j;) {
            if (nums[i] + nums[j] > -nums[k]) {
                j --;
            }else if (nums[i] + nums[j] < -nums[k]){
                i ++;
            }
            else {
                let tmp = [nums[k],nums[i],nums[j]];
                if (!map[tmp]){
                    map[tmp] = true;
                    ans.push(tmp);
                }
                i ++;
            }
        }
    }
    return ans;
};
function compare(a, b) {
  if (a < b ) {           // 按某种排序标准进行比较, a 小于 b
    return -1;
  }
  if (a > b ) {
    return 1;
  }
  // a must be equal to b
  return 0;
}
// @lc code=end

