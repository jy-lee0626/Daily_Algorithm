import sys

def fibo(n):
    global zero_cnt
    global one_cnt

    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        if len(dp) > n:
            return dp[n]
        else:
            a, b = fibo(n - 1)
            c, d = fibo(n - 2)
            dp.append([a + c, b + d])
            return dp[n]

n = int(sys.stdin.readline().rstrip())
dp = [[1, 0], [0, 1]]
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    print(*fibo(num))