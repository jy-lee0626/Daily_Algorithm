import sys

while(True):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    while(n>9):
        n = sum(map(int,list(str(n))))
    print(n)