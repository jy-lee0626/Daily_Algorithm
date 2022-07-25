N = int(input())

my_arr = set()
for i in range(N):
    my_word = str(input())
    asc = 0
    for j in my_word:
        asc *= 100
        asc += ord(j) 
    lst = [my_word, asc]
    my_arr.add(tuple(lst))

result = sorted(my_arr, key= lambda x: x[1])

for re in result:
    print(re[0])