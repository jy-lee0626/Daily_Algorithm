import sys

vowel = ['a', 'i', 'u', 'e', 'o']

while True:
  cnt = 0
  write = str(input().strip())
  if write == '#':
    break
  letter = write.lower()
  for i in letter:
    if i in vowel:
      cnt += 1
  print(cnt)