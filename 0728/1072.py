import sys 

def sol():

    n = 0
    start = int((win / total) * 100)
    z = start 
    while start == z:
        n += 1
        z = int(((win + n) / (total + n)) * 100)
    return n

total, win = map(int, sys.stdin.readline().split())
if total == win:
    print(-1)
else:
    print(sol())

