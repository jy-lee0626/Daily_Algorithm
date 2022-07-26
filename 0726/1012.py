import sys
from collections import deque

def BFS(x, y):
    queue = deque()                             # queue 반들고
    queue.append((x, y))                        # x, y queue에 넣기
    visited[x][y] = 1                           # 방문 표시하고
    
    while queue:
        x, y = queue.popleft()                  # queue 에서 x, y 꺼내고
        
        for i in range(4):                      # 동서남북 체크하고
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and my_arr[nx][ny] and not visited[nx][ny]:      # 범위 안에 들고, 배추가 있고, 방문한 적 없으면
                visited[nx][ny] = 1
                queue.append((nx, ny))          # queue에 추가


T = int(sys.stdin.readline())                   # test case number

for _ in range(T):  
    m, n, k = map(int, sys.stdin.readline().split())         # m: 가로 n: 세로 k:배추 갯수
    my_arr = [[0] * m for _ in range(n)]        # 배추밭
    visited = [[0] * m for _ in range(n)]       # 방문 체크
    dx = [-1, 0, 1, 0]                          # x 방향 벡터
    dy = [0, 1, 0, -1]                          # y 방향 벡터

    
    for _ in range(k):                          # 배추심기
        y, x = map(int, sys.stdin.readline().split())
        my_arr[x][y] = 1
    
    result = 0
    
    for x in range(n):
        for y in range(m):
            if my_arr[x][y] == 1 and not visited[x][y]:    # 배추가 있고, 방문한 적이 없으면 DFS 시작
                BFS(x, y)
                result += 1                                 # DFS로 배추 확인 끝나면 벌레 1마리 추가
            
    print(result)
