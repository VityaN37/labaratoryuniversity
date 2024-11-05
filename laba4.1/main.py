#Натуральные числа. Для каждого числа вывести используемые цифры (прописью) и их количество
import re
with open('file.txt', 'r') as file:
    content = file.read()
j=r'\s[1-9]\d*'
numbers = re.findall(j, content)

print(numbers)

for number in numbers:
        print(f"Число: {number}")
        digit_count = {} #digit count
        for i in number:
            digit_count[i] = digit_count.get(i, 0) + 1
        print(f"Количество цифр: {digit_count}")


