function findContentChildren(g: number[], s: number[]): number {
    let ans: number = 0;
    g.sort(compare)
    s.sort(compare)
    console.log(g,s);
    for (let i = 0,j = 0;i < g.length && j < s.length;){
        if (g[i] <= s[j]) {
            ans ++;
            i ++;
            j ++;
        }
        else j ++;
    }
    return ans;
};

function compare(a: number, b: number): number{
    // console.log(a,b);
    return a < b?-1:(a==b?0:1);
}