import sys

lst = [0] * 26

my_word = str(sys.stdin.read()).replace('\n', '').replace(" ", "")
# my_word = sys.stdin.read()

for word in my_word:
  lst[ord(word) - 97] += 1
  
max_num = max(lst)

for idx, i in enumerate(lst):
  if i == max_num:
    print(chr(idx + 97), end="")