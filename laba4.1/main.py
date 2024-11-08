#Натуральные числа. Для каждого числа вывести используемые цифры (прописью) и их количество
import re
with open('file.txt', 'r') as file:
    #numbers = file.readline()
    content = file.readline()

#j=r'\b[1-9][0-9]*\b'
#j=r'[1-9]\d*[^.|^\s]'
numbers = re.findall(r"\b[1-9]+[^.]", content)
print(numbers)
#l=re.findall(r"\b[^-][1-9]\d*",numbers)
#print(l)

for number in numbers:
        print(f"Число: {number}")
        digit_count = {} #digit count
        for i in number:
            digit_count[i] = digit_count.get(i, 0) + 1
        print(f"Количество цифр: {digit_count}")


