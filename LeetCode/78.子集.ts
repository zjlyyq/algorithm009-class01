var ans: number[][];
function subsets(nums: number[]): number[][] {
    ans = [];
    ans.push([]);
    subSetsProcess(nums, 0);

    return ans;
};


function subSetsProcess(nums: number[], level: number): void {
    // 递归终止条件
    if (level == nums.length) return;

    // 当前层逻辑
    ans.forEach(item => {
        let tmp: number[] = [];
        tmp = tmp.concat(item);
        tmp.push(nums[level]);
        ans.push(tmp);
    })

    subSetsProcess(nums, level + 1);
}