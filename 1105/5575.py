import sys

for _ in range(3):
  s = 0
  m = 0
  result = []
  sh, sm, ss, eh, em, es = map(int, sys.stdin.readline().split())
  
  if es - ss < 0:
    s += 1
    value = es - ss + 60
    result.insert(0, value)
  else:
    result.insert(0, es - ss)
    
  if em - sm - s< 0:
    m += 1
    value = em - sm + 60 - s
    result.insert(0, value)
  else:
    value = em - sm - s
    result.insert(0, value)
  
  value = eh - sh - m
  result.insert(0, value)
  print(*result)