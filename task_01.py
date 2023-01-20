#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open ('myfile.txt', 'r', encoding='utf-8') as f:
    some_list = f.read().split()
new_list = filter(lambda word: 'abc' not in word, some_list)
print(list(new_list))

