/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    // 根据列占用信息，对角线，反对角线判断落子是否合法
    function check(row, col) {
        for(let i = 0;i < cols.length;i ++) {
            if (cols[i] == col || lines[i] == row+col || lines_rev[i] == col-row){
                return false;
            }
        } 
        return true;
    }
    function output(cols) {
        let solve = []
        for(let i = 0;i < n;i ++) {
            let str = "";
            for(let j = 0;j < n;j ++) {
                str += (j == cols[i]?"Q":".");
            }
            solve.push(str)
        }
        ans.push(solve);
    } 
    function dfs(row) {
        if (row == n) {
            ans += 1;
        }
        for (let i = 0;i < n;i ++) {
            // 剪枝
            if (check(row, i)) {
                cols.push(i);
                lines.push(row+i);
                lines_rev.push(i-row);
                dfs(row+1);
                // 回溯
                cols.pop();
                lines.pop(); 
                lines_rev.pop();
            }
        }
    }
    let cols = [], lines = [], lines_rev = [], ans = 0;
    dfs(0);
    // console.log(ans)
    return ans;
};