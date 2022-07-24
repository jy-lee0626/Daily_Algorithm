import sys

sys.stdin = open('input.txt')

arr = list(map(int, input().split()))  # 주어진 list
T = len(arr)  # list 길이
num = 0   # 부분집합의 수

for i in range(1 << T):
    for j in range(T):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()
    num += 1
print(num)


<<<<<<< HEAD
=======


>>>>>>> ad8c79219617003e365cf5c82e3362709c0ec56b
