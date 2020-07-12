/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    let mask = 1;
    let ans = 0;
    for (let i = 0;i < 32;i ++){
        ans <<= 1;
        ans += n&1;
        mask <<= 1;
        n >>= 1;
    }
    return ans >>> 0;
};