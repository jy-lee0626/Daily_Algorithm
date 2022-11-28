import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n + 1)
dp[1] = 5

for i in range(2, n + 1):
  dp[i] = dp[i - 1] + ((i + 1) * 2 + i - 1)

print(dp[n] % 45678)


