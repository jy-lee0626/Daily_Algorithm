import sys
from collections import deque

def DFS(start):
    pass

def BFS(start):
    pass

sys.stdin = open('input.txt')

n, m, v = map(int, sys.stdin.readline().split())        # n: 정점의 갯수 m: 간선의 갯수 v: 정점의 번호
my_arr = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    my_arr[x].append[y]
    
print(my_arr)
