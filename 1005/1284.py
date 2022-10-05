import sys

while True:
  num = str(sys.stdin.readline().rstrip())
  result = 1
  
  if num == '0':
    break
  
  for i in num:
    if i == '1':
      result += 3
    elif i == '0':
      result += 5
    else:
      result += 4
  
  print(result)