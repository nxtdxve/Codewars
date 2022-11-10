# https://www.codewars.com/kata/5426d7a2c2c7784365000783/

def balanced_parens(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['()']
    else:
        result = []
        for i in range(n):
            for left in balanced_parens(i):
                for right in balanced_parens(n - 1 - i):
                    result.append('(' + left + ')' + right)
        return result
        