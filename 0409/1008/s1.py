cnt = 0
first_num = num = int(input())

while True:
    cnt += 1

    if num < 10:
        num = (num * 10 + num)
    else:
        a = num // 10
        b = num % 10
        if a + b >= 10:
            num = b * 10 + ((a + b) % 10)
        else:
            num = b * 10 + (a + b)

    if num == first_num:
        break

print(cnt)