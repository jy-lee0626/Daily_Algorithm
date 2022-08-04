import sys

my_str = str(sys.stdin.readline().rstrip())
result = ''

for i in my_str:
    if i.isupper():
        result += (i.lower())
    else:
        result += (i.upper())
        
print(result)