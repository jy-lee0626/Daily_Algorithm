import sys

def selling(money, sell, benefit):
  if sell >= benefit:
    return print(-1)
  else:
    profit = benefit - sell
    return print((money // profit) + 1)
  
money, sell, benefit = map(int, sys.stdin.readline().split())

selling(money, sell, benefit)
