function canJump(nums: number[]): boolean {
    return dfs(nums, 0);
};

function dfs(nums: number[], pos: number): boolean {
    if (pos + nums[pos] >= (nums.length-1)) return true;
    let flag: boolean = false;
    for (let i = 0;i < nums[pos];i ++) {
        flag = flag || dfs(nums, pos+i);
        if (flag) return true;
    }
    return false;
}
