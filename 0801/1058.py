import sys
from collections import deque

def Sol(start):
    stack = deque()
    
    for i in range(N):
        if my_arr[start][i] == 'Y':
            my_friends[start][i] = 1
            stack.append(i)
    
            
    while stack:
        friend = stack.popleft()
        for i in range(N):
            if my_arr[friend][i] =='Y' and i != start:
                my_friends[start][i] = 1
                

N = int(sys.stdin.readline().rstrip())

my_arr = [list(str(sys.stdin.readline().rstrip())) for _ in range(N)]
my_friends = [[0] * N for _ in range(N)]

for i in range(N):
    Sol(i)
    
result = 0

for i in range(N):
    num = my_friends[i].count(1)
    if num > result:
        result = num
        
print(result)
