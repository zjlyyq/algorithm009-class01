let cache: Number[] = [];
function canJump(nums: number[]): boolean {
    for(let i = 0;i < nums.length;i ++) {
        cache.push(0);
    }
    return true;
};

function dfs(nums: number[], pos: number): boolean {
    if (pos + nums[pos] >= (nums.length-1)) return true;
    for (let i = 1;i <= nums[pos];i ++) {
        if (cache[pos+i] == 1) return true;
        else if(cache[pos+1] == -1) continue;
        else {
            cache[pos+i] = dfs(nums, pos+i)?1:-1;
            if (cache[pos+i]) return true;
        }
    }
    return false;
}

