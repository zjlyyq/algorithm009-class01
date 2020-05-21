/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let filteredS = filterOutNumberAndChar(s);
    let reversedS = reverseString(filteredS);
    // console.log(filteredS);
    // console.log(reversedS);
    str = '';
    return filteredS.toUpperCase() == reversedS.toUpperCase()
};
console.log(isPalindrome("A man, a plan, a canal: Panama"))

function filterOutNumberAndChar(s){
    // return s.replace(/[^A-Za-z0-9]/g, '');
    return s.replace(/\W/g, '');
}
function reverseString(str) {
    return str.split("").reverse().join("");
    return joinArray;
}

// console.log(isPalindrome('dsdf..dwew2323;'))