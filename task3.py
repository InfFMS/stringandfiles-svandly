# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.

with open("task3.txt", "r", encoding="utf-8") as f:
    failik = f.read()
failik = failik.lower()
failik = failik.replace('.', '')
failik = failik.replace(',', '')
pippip = failik.split()
count = len(pippip)
w = 1
k = 0

sorted = sorted(pippip)

print(pippip, count)

# points = s.count('.')

slova = []
ciferki = []

for i in sorted:
    numbero = sorted.count(i)
    slova = [i, numbero] + slova

# print(slova)
#
#
# print(sorted)

with open("task3new.txt", "w", encoding="utf-8") as filenew:
    filenew.write(f"{slova}: {numbero}\n")