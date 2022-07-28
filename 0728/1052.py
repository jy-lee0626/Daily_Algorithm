import sys 

def sol(a, b):
    n = 0
    k = 1
    while a > b:
        if a % 2:
            n += k
            a = (a + 1) / 2
        else:
            a = a / 2
            
        k *= 2
        
    return n


a, b = map(int, sys.stdin.readline().split())
print(sol(a, b))