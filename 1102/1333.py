import sys

n, song, ring = map(int, sys.stdin.readline().split())
time = 0
length = song
repeat = ring


while True:
  if time >= n:
    print(repeat)
    break
  
  if length > repeat:
    while length > repeat:
      repeat += ring

  if length <= repeat < length + 5:
    print(repeat)
    break
  else:
    time += 1
    length += (song + 5)

