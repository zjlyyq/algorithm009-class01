let allOrder: Map<string,number[]>  = new Map();
let visted: boolean[] = [];
function permuteUnique(nums: number[]): number[][] {
    allOrder = new Map();
    visted = [];
    for(let i = 0;i < nums.length;i ++) {
        visted.push(false);
    }
    dfs(nums, 0, []);
    let ans: number[][] = []
    for (let [key, value] of allOrder) {
        // console.log(key);
        ans.push(value);
    }
    return ans;
};

function dfs(nums: number[], level: number, order: number[]):void {
    if (level == nums.length) {
        let t: string = "";
        for (let i of order){
            t += i;
        }
        let tmp: number[] = [];
        // if (allOrder.get(t) == undefined) {
        allOrder.set(t, tmp.concat(order));
        // }
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