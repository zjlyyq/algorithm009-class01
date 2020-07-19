/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let map = new Array(s.length);
    for(i = 0;i < s.length;i ++){
        map[i] = [];
        for (j = 0;j < s.length;j ++) {
            map[i].push(false);
        }
    }
    ans = "";
    for(let l = 0;l < s.length;l ++ ) {
        for (let i = 0;i + l < s.length;i ++) {
            let j = i+l;
            if(l == 0) {
                map[i][j] = true;
            }
            else if(l == 1) {
                map[i][j] = (s[i]==s[j]);
            }
            else {
                map[i][j] = map[i+1][j-1] && (s[i] == s[j]);
            }
            if (map[i][j]) {
                ans = s.substring(i,j+1) 
            }
        }
    }
    // console.log(ans)
    return ans;
};