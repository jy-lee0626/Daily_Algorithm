import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
  secret = str(sys.stdin.readline().rstrip())
  if 6 <= len(secret) <= 9:
    print('yes')
  else:
    print('no')