import sys
sys.stdin = open('input.txt')

T = int(input())
print(T)
my_list = list(map(int, input().split()))
print(my_list)

num = int(input())
my_list2 = []

for _ in range(num):
    my_list2.append(list(map(int, input().split())))
print(my_list2)

# 한 줄로도 가능!
my_list3 = [list(map(int, input().split()))]