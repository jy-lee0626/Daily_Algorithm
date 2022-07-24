N, m, M, T, R = map(int, input().split())
cnt = 0
heart = m
while N > 0:
    if M - m < T:
        cnt = -1
        break
    if heart + T <= M:
        heart += T
        cnt += 1
        N -= 1
    elif heart + T > M:
        if heart - R < m:
            heart = m
            cnt += 1
        else:
            heart -= R
            cnt += 1

print(cnt)
