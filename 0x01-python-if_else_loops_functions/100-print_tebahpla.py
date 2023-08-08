#!/usr/bin/python3
for ch in range(26):
    if ch % 2 == 0:
        print('{:c}'.format(122 - ch), end='')
    else:
        print('{:c}'.format(90 - ch), end='')
