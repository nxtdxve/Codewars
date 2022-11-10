# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/

def sort_array(source_array):
    odd = sorted([i for i in source_array if i % 2 != 0])
    return [odd.pop(0) if i % 2 != 0 else i for i in source_array]