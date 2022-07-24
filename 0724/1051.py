def sol(max_num):
    if max_num == 1:
        return 1
    
    while max_num > 1:
        for i in range(n - max_num + 1):
            for j in range(m - max_num + 1):
                if i + max_num - 1 <= n and j + max_num - 1 <= m:
                    if arr[i][j] == arr[i+max_num-1][j] == arr[i][j+max_num-1] == arr[i+max_num-1][j+max_num-1]:
                        return max_num**2
        
        max_num -= 1
    return 1
    

import sys
n, m = list(map(int, sys.stdin.readline().split()))

arr = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    arr.append([int(n) for n in s])

max_num = min(n, m)

print(sol(max_num))
