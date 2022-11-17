// https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/

// Solution 1
function solution(str){
    let arr = [];
    for (let i = 0; i < str.length; i += 2) {
      arr.push(str[i] + (str[i + 1] || '_'));
    }
    return arr;
  }


// Solution 2
function solution(str){
    let arr = [];
    for (let i = 0; i < str.length; i += 2) {
      arr.push(str.slice(i, i + 2));
    }
    return arr.map(x => x.length === 2 ? x : x + '_');
  }