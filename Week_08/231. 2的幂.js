/**
 * @param {number} n
 * @return {boolean}
 */
// 二进制数1出现的次数为1 --》 true
var isPowerOfTwo = function(n) {
    return n >0 && n == (n&-n);
};