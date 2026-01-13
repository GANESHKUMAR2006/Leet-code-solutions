/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    x=String(x)
    rev=x.split('').reverse().join('')
    return x==rev
};