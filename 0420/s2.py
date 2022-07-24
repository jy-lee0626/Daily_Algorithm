T = int(input())  # test case number


for tc in range(1, T+1):
    a, b = map(int, input().split())
    lst = []
    n = a
    while True:
        if n % 10 in lst:
            break
        lst.append(n % 10)
        n = n * a

    if len(lst) == 1:
        print(*lst)
    else:
        k = len(lst)
        m = b % k - 1
        print(lst[m])