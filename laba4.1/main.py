#Натуральные числа. Для каждого числа вывести используемые цифры (прописью) и их количество
import re
with open('file.txt', 'r') as file:
    content = file.read()
j=r'\d[1-9]'
numbers = re.findall(j, content)
print(numbers)