#Натуральные числа. Для каждого числа вывести используемые цифры (прописью) и их количество
import re
w =open('file.txt', 'r')
content = w.readline().split()
while True:
    for number in content:
        numbers=re.findall(r"^[1-9]\d*$",number)
        if numbers:
            print(f"Число: {number}")
            digit_count = {} #digit count
            for i in number:
                digit_count[i] = digit_count.get(i, 0) + 1
            print(f"Количество цифр: {digit_count}")

    content = w.readline().split()
    if content==[]:
        break
    #print(f"{number} не является натуральным числом.")






