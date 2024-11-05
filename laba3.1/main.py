#Натуральные числа. Для каждого числа вывести используемые цифры (прописью) и их количество
with open('fileint.txt', 'r') as file:
    while True:
        content = file.readline()
        numbers = content.split()
        for number in numbers:
            if number.isdigit():  # verification natural numbers
                print(f"Число: {number}")
                digit_count = {}  # digit count
                for i in number:
                    digit_count[i] = digit_count.get(i, 0) + 1
                print(f"Количество цифр: {digit_count}")
            else:
                print(f"{number} не является натуральным числом.")
        if not content:  # Если достигнут конец файла
            break





