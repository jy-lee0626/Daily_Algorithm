import sys

def Factorial(n):
  if 0 <= n < 2:
    return 1
  return n * Factorial(n - 1)
   

n = int(sys.stdin.readline().rstrip())

print(Factorial(n))
