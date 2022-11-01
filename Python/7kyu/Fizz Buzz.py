# https://www.codewars.com/kata/5300901726d12b80e8000498

def fizzbuzz(n):
    arr = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                arr.append("FizzBuzz")
            else:
                arr.append("Fizz")
        elif i % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(i)
    return arr