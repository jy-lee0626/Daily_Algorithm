T = int(input())

arr = []
for i in range(T):
    arr.append(input())

result = ''
k = 0
num = len(arr[0])

for i in range(num):
    check = 0
    for j in range(T - 1):
        if arr[j][i] != arr[j + 1][i]:
            check = 1
    if check:
        result += '?'
    else:
        result += arr[0][i]

print(result)
