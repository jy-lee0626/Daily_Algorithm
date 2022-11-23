import sys

my_word = str(sys.stdin.readline().rstrip())
secret_word = str(sys.stdin.readline().rstrip())
repeat = len(secret_word)
result = ''
# a = 97, z = 122
for idx, word in enumerate(my_word):
  count = ord(word) - ord(secret_word[idx%repeat])
  if word == ' ':
    result += ' '
  elif count <= 0:
    result += chr(122 + count)
  elif count > 0:
    result += chr(count + 96)
print(result)