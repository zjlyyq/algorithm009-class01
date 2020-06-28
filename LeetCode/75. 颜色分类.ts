/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    let l = 0;
    let r = nums.length - 1;

    for (let i = 0;i < r;i ++) {
        if (nums[i] == 0) {
            let tmp = nums[i];
            nums[i] = nums[l];
            nums[l++] = tmp;
        }
        else if (nums[i] == 2){
            let tmp = nums[i];
            nums[i] = nums[r];
            nums[r--] = tmp;
            // 从后面交换过来还没检查过
            i --;
        }
    }
};