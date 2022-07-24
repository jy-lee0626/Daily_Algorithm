# lst = []
# for i in range(5, -1, -1):
#     lst.append(11 * i)
# print(lst)

# lst_2 = ['A', 'B', 'T', 'A', 'A', 'A', 'B', 'A', 'A']
# lst_2 = set(lst_2)
# lst_2 = sorted(list(lst_2))
# print(lst_2)

# def k(x):
#     if x > 10:
#         return
#
#     if x >= 6:
#         print(x)
#         k(x - 1)
#     else:
#         k(x + 1)

# def k(x):
#     if x < 6:
#         return
#     print(x)
#     k(x - 1)
#     print(x)
#
# k(10)

def bfs(x, y):
    q = []
    q.append((x, y, 1))
    while q:
        x, y, cnt = q.pop(0)
        visited[x][y] = 1
        arr[x][y] = cnt
        for i, j in [(-1, 0 ), (1, 0), (0, 1), (0, -1)]:
            ni = x + i
            nj = y + j
            if 0 <= ni < 4 and 0 <= nj < 4 and not visited[ni][nj]:
                q.append((ni, nj, cnt + 1))

arr = [[0] * 4 for _ in range(4)]
visited = [[0] * 4 for _ in range(4)]
bfs(1, 1)
print(arr)
