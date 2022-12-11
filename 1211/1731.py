# import sys

# def Plus(time, value, before):
#   print(time, value, before)
#   for i in range(time):
#     next = int(sys.stdin.readline().rstrip())
#     if next - before != value:
#       return
#     else:
#       before = next
#   return print(before + value)

# def Ratio(time, value, before):
#   print(time, value, before)
#   for i in range(time):
#     next = int(sys.stdin.readline().rstrip())
#     if next // before != value:
#       return
#     else:
#       before = next
#   return print(before * value)

# N = int(sys.stdin.readline().rstrip())
# P = int(sys.stdin.readline().rstrip())
# Q = int(sys.stdin.readline().rstrip())
# equal_difference = Q - P
# equal_ratio = Q // P
# Plus(N - 2, equal_difference, Q)
# Ratio(N - 2, equal_ratio, Q)

li = []
for _ in range(int(input())):
    li.append(int(input()))
    
ans = li[-1]
if li[2]-li[1] == li[1]-li[0]:
    ans += (li[1]-li[0])
elif li[2]//li[1] == li[1]//li[0]:
    ans *= (li[1]//li[0])

print(ans)