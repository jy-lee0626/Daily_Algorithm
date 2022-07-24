def solve(my_str1, my_str2):
    N = len(my_str1)
    M = len(my_str2)
    i = 0
    while i < M:
        if N != M:
            return False
        elif my_str1[i] != my_str2[i]:
            return False
        i += 1
    return True

import sys

sys.stdin = open('input.txt')

my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2))



