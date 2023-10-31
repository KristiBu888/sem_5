# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# решение 1
a = 3
b = 5


def power(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * power(a, b - 1))


print(power(a, b))


# решение 2
def f(a, b):
    if b == 0:
        return 1
    return f(a, b - 1) * a


print(f(a=3, b=5))
