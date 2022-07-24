N, L = map(str, input().split())
lst = []
num = 1
while len(lst) < int(N):
    if L in str(num):
        num += 1
    else:
        lst.append(num)
        num += 1

print(lst[-1])
