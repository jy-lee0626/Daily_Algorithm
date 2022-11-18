import sys

end = list(map(int, sys.stdin.readline().rstrip().split(":")))
start = list(map(int, sys.stdin.readline().rstrip().split(":")))
end_second = end[0] * 3600 + end[1] * 60 + end[2]
start_second = start[0] * 3600 + start[1] * 60 + start[2]
if end_second > start_second:
  start_second += 24 * 3600
remain_time = start_second - end_second
result = ""
H = remain_time // 3600
if H < 10:
  result += '0' + str(H) + ':'
else:
  result += str(H) + ':'
remain_time -= H * 3600
M = remain_time // 60
if M < 10:
  result += '0' + str(M) + ':'
else:
  result += str(M) + ':'
remain_time -= M * 60
if remain_time < 10:
  result += '0' + str(remain_time)
else:
  result += str(remain_time)
print(result)
