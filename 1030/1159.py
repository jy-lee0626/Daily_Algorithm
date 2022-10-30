import sys

n = int(sys.stdin.readline().rstrip())
lst = list(range(ord('a'), ord('z') + 1))
alpabet = [0] * 26

for i in range(n):
  check = str(sys.stdin.readline().rstrip())[0]
  alpabet[ord(check) - 97] += 1

cnt = 0
for idx, num in enumerate(alpabet):
  if num >= 5:
    print(chr(idx + 97), end='')
    cnt += 1

if not cnt:
  print('PREDAJA')