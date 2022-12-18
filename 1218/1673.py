import sys

# while True:
#   try:
#     n ,k = map(int, sys.stdin.readline().split())
#     stamp = n
    
#     while True:
#       if (stamp//k==0):
#         break
#       n += stamp//k
#       stamp = stamp//k + stamp % k
      
#       print(n)
#   except EOFError:
#     break

# while True:
#   try:
#     n ,k = map(int, sys.stdin.readline().split())
#     coupon = n
#     result = n

#     while True:
#       if coupon > k:
#         coupon -= k - 1
#         result += 1
#       else: 
#         break

#     print(result)
#   except EOFError:
#     break

for i in sys.stdin.readlines():
    n,k=map(int,i.strip().split())
    t=0
    r=0
    while n>=k:
        t=n//k
        r+=k*t
        n=n%k+t
    r+=n
    print(r)