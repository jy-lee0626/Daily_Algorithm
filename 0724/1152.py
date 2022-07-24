def sol(txt):
    if txt =='':
        cnt = 0
        return cnt
    else:
        cnt = 1
        for i in txt:   
            if i == ' ':
                cnt += 1
        return cnt

txt = input()
txt = txt.strip()

print(sol(txt))