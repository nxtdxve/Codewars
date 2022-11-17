// https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/

function solution(str){
    let arr = [];
    for (let i = 0; i < str.length; i += 2) {
      arr.push(str[i] + (str[i + 1] || '_'));
    }
    return arr;
  }