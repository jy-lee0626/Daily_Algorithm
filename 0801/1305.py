import sys
from collections import deque

num = int(sys.stdin.readline().rstrip())
ad = list(map(str, sys.stdin.readline().rstrip()))

stack = deque()
for i in ad:
    stack.append(i)

my_arr = set()

for i in range(num):
    my_str = ''
    new_stack = deque()
    while stack:
        new = stack.popleft()
        my_str += str(new)
        new_stack.append(new)
    my_arr.add(my_str)
    stack = new_stack
    a = stack.popleft()
    stack.append(a)
    
for i in my_arr:
    n = 0
    for j in range(num):
        if i[j] == i[-1]:
            n += 1