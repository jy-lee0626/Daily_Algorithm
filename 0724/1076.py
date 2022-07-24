Dic = {
    'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,
    'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9
    }

# print(Dic.get('black'))

st = input()
nd = input()
rd = input()

first = Dic.get(st)
second = Dic.get(nd)
third = Dic.get(rd)

result = (first * 10 + second) * 10**third
print(result)