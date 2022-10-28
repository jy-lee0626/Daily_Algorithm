import sys

num = int(sys.stdin.readline().rstrip())

k = 1
t = 1
n = 1
m = 1
a = 0

while k < num:
  if a:
    if m == 1:
      n += 1
      a -= 1
    else:
      m -= 1
      n += 1
  else:
    if n == 1:
      m += 1
      a += 1
    else:
      n -= 1
      m += 1
  k += 1
    
print('{}/{}'.format(n, m))