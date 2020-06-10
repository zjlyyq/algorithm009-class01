function canJump(nums: number[]): boolean {
    let d = 0;
    for(let i = 0;i < nums.length;i ++) {
        if (i <= d) {
            d = Math.max(d, i + nums[i]);
            if (d >= nums.length - 1) return true;
        }
    }
    return false;
};
