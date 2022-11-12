import sys

n = int(sys.stdin.readline())

# def divide3(value, n):
#   global result
#   if n > result:
#     return
#   if value == 1:
#     if n < result:
#       result = n
#   n += 1
#   value //= 3
  
#   if not value % 3:
#     divide3(value, n)
#   if not value % 2:
#     divide2(value, n)
#   minus(value, n)

# def divide2(value, n):
#   global result
#   if n > result:
#     return
  
#   if value == 1:
#     if n < result:
#       result = n
#   n += 1
#   value //= 2
  
#   if not value % 3:
#     divide3(value, n)
#   if not value % 2:
#     divide2(value, n)
#   minus(value, n)
#   return

# def minus(value, n):
#   global result
#   if n > result:
#     return
#   if value == 1:
#     if n < result:
#       result = n
#   n += 1
#   value -= 1
  
#   if not value % 3:
#     divide3(value, n)
#   if not value % 2:
#     divide2(value, n)
#   minus(value, n)
#   return 

# if not num % 3:
#   divide3(num, 0)
  
# if not num % 2:
#   divide2(num, 0)

# minus(num, 0)

# print(result)

dp=[0]*(n+3)
dp[1],dp[2],dp[3]=0,1,1
for i in range(4,n+1):
    if i%2==0 and i%3==0:
        dp[i]=min(dp[i//3],dp[i//2],dp[i-1])+1
    elif i%3==0:
        dp[i] = min(dp[i // 3],dp[i-1]) + 1
    elif i%2==0:
        dp[i] = min(dp[i // 2],dp[i-1]) + 1
    else:
        dp[i]=dp[i-1]+1
print(dp[n])