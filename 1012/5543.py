import sys

hambur = []
beverage = []

for i in range(5):
  if i < 3:
    hambur.append(int(sys.stdin.readline().rstrip()))
  else:
    beverage.append(int(sys.stdin.readline().rstrip()))

print(min(hambur) + min(beverage) - 50)
