# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.


with open("task2.txt", "r", encoding="utf-8") as f:
    makaka = f.read()

pitonzamena = makaka.replace("Python", "Питон")

with open("piton.txt", "w", encoding="utf-8") as newfile:
    newfile.write(pitonzamena)

count = makaka.count("Python")

print("Количество произведенных замен:", count)