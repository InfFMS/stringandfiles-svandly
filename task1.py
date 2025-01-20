# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
with open('task1.txt', encoding='utf-8') as f:
s=f.read()
print(len(s))
worlds = s.split(' ')
points = s.count('.')
dash = s.count('—')
g = len(worlds)
j = g - points - dash
strings = s.count('\n')
print(j)
print(strings + 1)