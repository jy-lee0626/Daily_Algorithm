import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
result = 0
pack_lst = []
guitar_lst = []

for i in range(m):
  pack, piece = map(int, sys.stdin.readline().rstrip().split())
  pack_lst.append(pack)
  guitar_lst.append(piece)
  
pack_lst.sort()
guitar_lst.sort()

guitar = n

while guitar > 0:
  if guitar > 6:
    if pack_lst[0] < guitar_lst[0] * 6:
      result += pack_lst[0]
      guitar -= 6
    else:
      result += guitar_lst[0] * 6
      guitar -= 6
  else:
    if pack_lst[0] < guitar_lst[0] * guitar:
      result += pack_lst[0]
      guitar = 0
    else:
      result += guitar_lst[0] * guitar
      guitar = 0
      
print(result)