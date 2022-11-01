# https://www.codewars.com/kata/520b9d2ad5c005041100000f/

def pig_it(text):
    return ' '.join([i[1:] + i[0] + 'ay' if i.isalpha() else i for i in text.split()])
    