#Натуральные числа. Для каждого числа вывести используемые цифры (прописью) и их количество
with open('fileint.txt', 'r') as file:
    content = file.read()
    numbers = content.split()

for number in numbers:
    if number.isdigit():  # verification natural numbers
        print(f"Число: {number}")
        digit_count = len(number) #digit count
        print(f"Цифры числа: {' '.join(number)}")  #split number
        print(f"Количество цифр: {digit_count}")
    else:
        print(f"{number} не является натуральным числом.")

