import sys

DNA = [[0, 2, 0, 1], [2, 1, 3, 0], [0, 3, 2, 1], [1, 0, 1, 3]]
dic = {'A': 0, 'G': 1, 'C' : 2, 'T' : 3}
N = int(sys.stdin.readline().rstrip())
secret = str(sys.stdin.readline().rstrip())
num_secret = ''

# 숫자로 바꾸는 부분 때문에 시간초과
for val in secret:
  num_secret += str(dic.get(val))

n = 1
end_num = int(num_secret[-1])

while n < N:
  # 시간초과
  # a, b = int(num_secret[-2]), int(num_secret[-1])
  # num_secret = num_secret[0:-2] + str(DNA[a][b])
  
  next_num = int(num_secret[-n-1])
  end_num = DNA[next_num][end_num]
  n += 1
  
# result = [k for k, v in dic.items() if v == end_num]
# print(*result)
if not end_num:
  print('A')
elif end_num == 1:
  print('G')
elif end_num == 2:
  print('C')
else:
  print('T')