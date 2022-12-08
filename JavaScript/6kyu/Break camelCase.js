// https://www.codewars.com/kata/5208f99aee097e6552000148/

// Solution 1
function solution(string) {
    let result = '';
    for (let i = 0; i < string.length; i++) {
        if (string[i] === string[i].toUpperCase()) {
            result += ' ' + string[i];
        } else {
            result += string[i];
        }
    }
    return result;
}

// Solution 2
function solution(string) {
    return string.replace(/([A-Z])/g, ' $1');
}

