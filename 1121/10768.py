import sys

month = int(sys.stdin.readline())
day = int(sys.stdin.readline())

if month < 2:
    print('Before')
elif month > 2:
    print('After')
elif day < 18:
    print('Before')
elif day > 18:
    print('After')
else:
    print('Special')