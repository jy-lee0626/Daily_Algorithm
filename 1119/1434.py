import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
box_list = deque(list(map(int, sys.stdin.readline().split())))
book_list = deque(list(map(int, sys.stdin.readline().split())))
now_box = 0
now_book = 0
result = 0
while now_book < M:
  if book_list[now_book] <= box_list[now_box]:
    box_list[now_box] -= book_list[now_book]
    now_book += 1
  else:
    now_box += 1
for i in box_list:
  result += i
print(result)
