def repeated(text):
    my_text = []
    for i in text:
        my_text.append(i)

    j = 0
    while j < len(my_text) - 1:
        if my_text[j] == my_text[j + 1]:
            # my_text.remove(my_text[j])
            # my_text.remove(my_text[j])
            my_text.pop(j)
            my_text.pop(j)
            j = 0
        else:
            j += 1
    return len(my_text)

import sys

sys.stdin = open('input.txt')

T = int(input())  # test case number

for tc in range(1, T+1):
    text = input()
    print('#{} {}'.format(tc, repeated(text)))

