# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.
print('Сколько предложений вы хотите ввести?')
num = int(input())
k = 0
ddddd = 0
with open("task4.txt", "w", encoding="utf-8") as f:

    while k < num:
        sent = input()
        ddddd = sent.replace(" ", "_")
        f.write(f"{ddddd}\n")
        k += 1

with open("task4.txt", "r", encoding="utf-8") as f_new:
    s = f_new.read()

print(s)