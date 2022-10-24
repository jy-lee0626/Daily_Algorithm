import sys

student, end = map(int, sys.stdin.readline().split())
lst = set()

for i in range(student):
    a = int(sys.stdin.readline())
    k = end // a
    for i in range(1, k + 1):
        lst.add(a * i)

print(len(lst))