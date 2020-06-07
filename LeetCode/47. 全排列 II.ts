let allOrder: Map<number[],boolean>  = new Map();
let visted: boolean[] = [];
function permuteUnique(nums: number[]): number[][] {
    allOrder = [];
    visted = [];
    for(let i = 0;i < nums.length;i ++) {
        visted.push(false);
    }
    dfs(nums, 0, []);
    let ans: number[][] = []
    for (let (key, value) of allOrder) {
        ans.push(key);
    }
    return ans;
};

function dfs(nums: number[], level: number, order: number[]):void {
    if (level == nums.length) {
        let t: number[] = [];
        t = t.concat(order);
        if (allOrder.get(t) == undefined) {
            allList.set(t, true);
        }
        return;
    }

    for(let i = 0;i < nums.length;i ++) {
        if (!visted[i]) {
            visted[i] = true;
            order.push(nums[i]);
            dfs(nums, level + 1, order);
            visted[i] = false;
            order.pop();
        }
    }
}