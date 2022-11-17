// https://www.codewars.com/kata/577b9960df78c19bca00007e/

var findDigit = function(num, nth){
    if (nth <= 0) return -1;
    let digits = Math.abs(num).toString().split('').reverse();
    return digits[nth - 1] ? +digits[nth - 1] : 0;
  }