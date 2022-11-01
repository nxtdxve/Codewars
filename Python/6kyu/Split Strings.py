# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    if len(s) % 2:
        s += "_"
    split: list = []
    while s:
        split.append(s[:2])
        s = s[2:]
    return split