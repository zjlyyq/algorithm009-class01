/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    if(s == ""){
        return true;
    }
    let s_string = '';
    for(let c of s){
        if((c>="a" && c <= 'z') || (c>="A" && c <= 'Z') || (c>="0" && c <= '9')) {
            s_string += c;
        }
    }
    s_string = s_string.toUpperCase();
    let len = s_string.length;
    for(let i = 0;i < s_string.length/2; i ++) {
        if (s_string[i] != s_string[len-i-1]) {
            return false;
        }
    }
    return true;
};
console.log(isPalindrome("0P"))