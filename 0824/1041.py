import sys

# 3면 -> 4개, 2면 -> n ** 3 - ( 4 * (n - 2) * (n - 1) + (n - 2) ** 2 + ((n - 2) ** 2 * (n - 1)) + 4), 0면 -> ((n - 2) ** 2) * (n - 1), 1면 -> 4 * (n - 2) * (n - 1) + (n - 2) ** 2
n = int(sys.stdin.readline().rstrip())
dice = list(map(int, sys.stdin.readline().split()))
if n == 1:
  dice.sort()
  result = sum(dice[0:5])
  print(result)
else:
  a_face = min(dice[0], dice[5])
  b_face = min(dice[1], dice[4])
  c_face = min(dice[2], dice[3])
  my_lst = [a_face, b_face, c_face]
  my_lst.sort()

  result = (my_lst[0] * (4 * (n - 2) * (n - 1) + (n - 2) ** 2)) + (my_lst[1] + my_lst[0]) * (n ** 3 - ( 4 * (n - 2) * (n - 1) + (n - 2) ** 2 + ((n - 2) ** 2 * (n - 1)) + 4)) + ((my_lst[2] + my_lst[0] + my_lst[1]) * 4)
  print(result)
