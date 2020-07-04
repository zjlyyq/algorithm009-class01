/**
 * @param {number} n
 * @return {number}
 */
var solveNQueens = function(n) {
    // 根据列信息，对角线信息，反对角线信息判断落子是否合法
    function check(row, col, cols, lines, lines_rev) {
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
    function dfs(row, cols, lines, lines_rev) {
        if (row == n) {
            output(cols);
        }
        for (let i = 0;i < n;i ++) {
            if (check(row, i, cols, lines, lines_rev)) {
                dfs(row+1, cols.concat([i]), lines.concat(row+i), lines_rev.concat(i-row));
            }
        }
    }
    let ans = []
    dfs(0, [], [], []);
    return ans;
};