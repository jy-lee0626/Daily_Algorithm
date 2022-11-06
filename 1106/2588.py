import sys

a = int(sys.stdin.readline().rstrip())
b = str(sys.stdin.readline().rstrip())

print(a * int(b[-1]))
print(a * int(b[-2]))
print(a * int(b[0]))
print(a * int(b))