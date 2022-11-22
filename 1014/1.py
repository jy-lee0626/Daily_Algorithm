source = 'execute'

# while source:
#     lst = list(range(ord('a'), ord('z') + 1))
#     removed_word = []

#     for word in source:
#         if ord(word) in lst:
#             lst.remove(ord(word))
#             removed_word.append(ord(word))
#             source.replace(word, '', 1)
#             print(source, word)
source = source.replace('e', '', 1)
print(source)