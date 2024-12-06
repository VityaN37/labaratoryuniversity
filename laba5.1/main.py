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
    F_2,F_1,p ,result= 1 , 1 ,1,0
    for i in range(2,n + 1):
        fact=fact*(2*i)*((2*i)-1)
        result=p * (F_1 + 2 * F_2 /fact)
        F_2=F_1
        F_1=result
        p*=-1
    return result

print(A(n,2))

time_func1 = timeit.timeit(lambda: A(n,2), number=1)
print("algorithmically")
print(time_func1)
time_func2 = timeit.timeit(lambda: F(n), number=1)
print("function")
print(time_func2)

if time_func1>time_func2:
    print("Функционально программа быстрее")
else:
    print("Алгоритмически программа выполняется быстрее")