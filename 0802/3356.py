import sys

def minStr(arr):
    length = len(arr)
    p = [0] * length
    j = 0
    for i in range(1, length):
        while j > 0 and arr[i] != arr[j]:
            j = p[j - 1]
            
        if arr[i] == arr[j]:
            j += 1
            p[i] = j
    
    return length - p[-1]

S = int(sys.stdin.readline().rstrip())
my_arr = list(str(sys.stdin.readline().rstrip()))


print(minStr(my_arr))

