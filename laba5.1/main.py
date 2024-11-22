#16.F(0) = 1, F(1) = 1, F(n) = (-1)n*(F(n–1) + 2*F(n-2) /(2n)!), при n > 1
from math import factorial
import timeit
def F(n):
    if n == 0 or n == 1:
        return 1  # Определите базовый случай для F(0) # Определите базовый случай для F(1)
    else:
        return (-1)**n * (F(n-1) + 2 * F(n-2) / factorial(2*n))


print("введите натуральное число : ")
n=int(input())
print(F(n))


def A(n,fact):
    if n==0 or n==1:
        return 1
    for i in range(2, 2*n + 1):
        fact *= i

    return (-1)**n * (F(n-1) + 2 * F(n-2) / fact)

print(A(n,1))

time_func1 = timeit.timeit(lambda: A(5,1), number=1)
print("algorithmically")
print(time_func1)
time_func2 = timeit.timeit(lambda: F(5), number=1)
print("function")
print(time_func2)

if time_func1>time_func2:
    print("Функционально программа быстрее")
else:
    print("Алгоритмически программа выполняется быстрее")