// https://www.codewars.com/kata/5300901726d12b80e8000498/

// solution 1
function fizzbuzz(n)
{
    var arr = [];
    for (var i = 1; i <= n; i++) {
        var str = '';
        if (i % 3 == 0) str += 'Fizz';
        if (i % 5 == 0) str += 'Buzz';
        if (str == '') str = i;
        arr.push(str);
    }
    return arr;
}

// solution 2
function fizzbuzz(n)
{
    var arr = [];
    for (var i = 1; i <= n; i++) {
        arr.push(i % 15 == 0 ? 'FizzBuzz' : i % 3 == 0 ? 'Fizz' : i % 5 == 0 ? 'Buzz' : i);
    }
    return arr;
}

console.log(fizzbuzz(19));



