#!/usr/bin/python3
def remove_char_at(str, n):
    num = 0
    new_str = ""
    for ch in str:
        if num != n:
            new_str += ch
        num += 1
    return new_str
