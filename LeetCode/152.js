// 动态规划
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    max = -100000000;
    lastMax = nums[0];
    lastMin = nums[0];
    let tmpMax = nums[0],tmpMin = nums[0];
    max = max > tmpMax?max:tmpMax;
    for(let i = 1; i < nums.length; i ++){
        if(nums[i] >= 0){
            tmpMax = lastMax*nums[i];
            tmpMax = tmpMax > nums[i]?tmpMax:nums[i];
            tmpMin = lastMin*nums[i];
            tmpMin = tmpMin < nums[i]?tmpMin:nums[i];
            max = max > tmpMax?max:tmpMax;
        }else {
            tmpMax = lastMin*nums[i];
            tmpMax = tmpMax > nums[i]?tmpMax:nums[i];
            tmpMin = lastMax*nums[i];
            tmpMin = tmpMin < nums[i]?tmpMin:nums[i];
            max = max > tmpMax?max:tmpMax;
        }
        lastMax = tmpMax;
        lastMin = tmpMin;
    }
    return max;
};

console.log(maxProduct([0,2]))