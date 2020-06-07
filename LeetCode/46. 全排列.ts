let allOrder: number[][] = [];
let visted: boolean[] = [];
function permute(nums: number[]): number[][] {
    allOrder = [];
    visted = [];
    for(let i = 0;i < nums.length;i ++) {
        visted.push(false);
    }
    dfs(nums, 0, []);
    return allOrder;
};

function dfs(nums: number[], level: number, order: number[]):void {
    if (level == nums.length) {
        let t: number[] = [];
        allOrder.push(t.concat(order));
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