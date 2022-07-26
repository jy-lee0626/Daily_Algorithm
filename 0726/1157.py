def sol(new_arr):
    if len(new_arr) > 1:
        a = new_arr.pop(0)
        b = new_arr.pop(0)
        if a[0] == b[0]:
            return print('?')
        else:
            return print(a[1])
    else:
        a = new_arr.pop()
        return print(a[1])
        

my_word = str(input()).upper()
my_arr = []

for i in my_word:
    if i not in my_arr:
        my_arr.append(i)
        
new_arr = []

for i in my_arr:
    num = my_word.count(i)
    new_arr.append([num, i])
    
new_arr.sort(reverse=True)

sol(new_arr)











