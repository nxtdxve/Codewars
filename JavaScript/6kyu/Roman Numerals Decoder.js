// https://www.codewars.com/kata/51b6249c4612257ac0000005/

// Solution 1
function solution(roman){
    const romanToNum = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    };
    let result = 0;
    for (let i = 0; i < roman.length; i++) {
        if (romanToNum[roman[i]] < romanToNum[roman[i + 1]]) {
            result -= romanToNum[roman[i]];
        } else {
            result += romanToNum[roman[i]];
        }   
    }
    return result;
}

// Solution 2
function solution(roman){
    const lookup = {I:1,V:5,X:10,L:50,C:100,D:500,M:1000}
    let number = 0
    let lastVal = 0
    for (let i = roman.length - 1; i >= 0; i--) {
        val = lookup[roman[i]]
        if (val < lastVal) {
            number -= val
        } else {
            number += val
        }
        lastVal = val
    }
    return number
}

// Solution 3
function solution(roman) {
    // Erstelle ein Objekt mit den römischen Ziffern und ihren dezimalen Werten
    const romanToDecimalMap = {
      I: 1,
      V: 5,
      X: 10,
      L: 50,
      C: 100,
      D: 500,
      M: 1000,
    };
    let decimal = 0;
  
    for (let i = roman.length - 1; i >= 0; i--) {
      const currentDecimal = romanToDecimalMap[roman[i]];
      const nextDecimal = romanToDecimalMap[roman[i + 1]];
      if (nextDecimal > currentDecimal) {
        decimal -= currentDecimal;
      } else {
        decimal += currentDecimal;
      }
    }

    return decimal;
  }