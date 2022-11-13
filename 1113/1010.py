import sys

def factorial(num):
  n = 1
  for i in range(num, 1, -1):
    n *= i
  return n

N = int(sys.stdin.readline())

for i in range(N):
  k, n = map(int, sys.stdin.readline().split())
  result = factorial(n) // (factorial(k) * factorial(n - k))
  print(result)