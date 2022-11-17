// https://www.codewars.com/kata/526c7363236867513f0005ca/

// Solution 1
function isLeapYear(year) {
    return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
  }

// Solution 2
function isLeapYear(year) {
    return new Date(year, 1, 29).getDate() === 29;
  }