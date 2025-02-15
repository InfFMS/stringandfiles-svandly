# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.

with open('task5.txt', encoding='utf-8') as f:
    s = f.read()
    # print(len(s))
    w = s.split(' ')
    max = 0
    for i in w:
        d = len(i)
        if d > max:
            max = d
            slovo = i

file = open('newfile.txt', 'w')
file.write(slovo, max)
file.close()
print(slovo)
print(max)