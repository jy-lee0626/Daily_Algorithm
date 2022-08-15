import sys

sys.stdin = open('input.txt')

def max_find(n, k, lst):
    length = len(lst)
    if n < 10:
        return -1
    x = 0
    a = 0
    while x < k:
        if a + 1 == length:
            if x % 2:
                if lst[0] == '0':
                    return -1
                return "".join(lst)
            else:
                lst[a - 1], lst[a] = lst[a], lst[a - 1]
                if lst[0] == '0':
                    return -1
                return "".join(lst)
        max_num = max(lst[a:])
        idx = 1
        while True:
            if lst[-idx] == max_num:
                break
            else:
                idx += 1
        max_idx = length - idx

        if a == max_idx:
            x -= 1
        else:
            lst[a], lst[max_idx] = lst[max_idx], lst[a]
        x += 1
        a += 1

    if lst[0] == 0:
        return -1
    return "".join(lst)



n, k = map(int, sys.stdin.readline().split())
lst = []
num = n
while num > 0:
    a = num % 10
    lst.append(str(a))
    num = num // 10

lst.reverse()

print(max_find(n, k, lst))
