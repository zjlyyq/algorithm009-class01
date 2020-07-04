let ans:number[] = [];
function superEggDrop(K: number, N: number): number {
    dfs(0,N,0);
    let ret = 0;
    for (let i = 0;i < ans.length;i ++) {
        if (ans[i] > ret) {
            ret = ans[i];
        }
    }

    return ret;
};

function dfs(left: number, right:number, k: number, count: number): void{
    if (left == right) {
        ans.push(left==0?count:count+1);
        return;
    }
    dfs(left, Math.round(right/2) -1, k-1, count+1);
    dfs(Math.round(right/2)+1, right, k, count+1);
}