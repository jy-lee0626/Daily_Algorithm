# 1. 반복문 활용
def solve(word):
    N = len(word)
    reverse_word = ''
    for i in range(N):
        reverse_word += word[N - i - 1]
    return reverse_word

# 2. pythonic (slicing)
def solve2(word2):
    new = word2[::-1]
    return new

import sys

sys.stdin = open('input.txt')

word = input()
print(solve(word))

word2 = input()
print(solve2(word2))

