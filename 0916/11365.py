import sys

sys.stdin = open('input.txt')

while True:
  word = str(sys.stdin.readline().rstrip())
  
  if word[0:3] == 'END':
    break
  print(word[-1:0:-1] + word[0])