/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let n = s.length, m = p.length;
    let dp = new Array(n+1).fill(null).map(()=>new Array(m+1).fill(false));
    for(let i = 0;i < m+1;i ++) {
        dp[0][0] = true;
        if (p[i] != "*") {
            break;
        }
        dp[0][i+1] = true;
    }
    for(let i = 1;i <= n;i ++) {
        for (let j = 1;j <= m;j ++) {
            if (s[i-1] == p[j-1] || p[j-1]=="?") {
                dp[i][j] = dp[i-1][j-1];
            }else {
                if (p[j-1] == "*") {
                    dp[i][j] = dp[i][j-1] || dp[i-1][j] ||  dp[i-1][j-1];
                }
                else{
                    dp[i][j] = false;
                }
            }
        }
    }
    return dp[n][m]
};