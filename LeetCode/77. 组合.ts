let allList: number[][] = [];
let visted: boolean[] = [];

function combine(n: number, k: number): number[][] {
    allList = [];
    for (let i = 0;i < n;i ++) visted.push(false);
    dfs(n, k, 0,-1,[]);
    return allList;
};

function dfs(n: number, k:number, level: number,start: number, arr: number[]):void{
    if (level == k) {
        let t:number[] = [];
        t = t.concat(arr);
        allList.push(t);
    }

    for (let i = start+1;i < n;i ++) {
        if (!visted[i]) {
            visted[i] = true;
            arr.push(i+1);
            dfs(n, k, level + 1,i, arr);
        }
        // 回溯
        arr.pop();
        visted[i] = false;
    }
}