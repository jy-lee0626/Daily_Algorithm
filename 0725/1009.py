import sys

sys.stdin = open('input.txt')

T = int(input())  # test case number

for i in range(T):
    arr = [
        [10],
        [1],
        [2,4,8,6],
        [3,9,7,1],
        [4,6],
        [5],
        [6],
        [7,9,3,1],
        [8,4,2,6],
        [9,1],
        [10]
    ]
    a, b = map(int, input().split())
    x = a % 10
    y = b % len(arr[x]) - 1
    print(arr[x][y])