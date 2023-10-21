import numpy as np
from scipy.optimize import minimize

# Определим функцию, минимум которой мы хотим найти
def func(x):
    return x**2 + 2*x + 1

# Зададим начальное приближение
x0 = 0

# Используем функцию minimize из scipy.optimize для нахождения минимума функции
result = minimize(func, x0)

# Выведем результат
print(result.x)
