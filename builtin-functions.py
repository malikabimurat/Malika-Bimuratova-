import time
import math
from functools import reduce

# 1. Умножение всех чисел в списке
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)

# 2. Подсчет количества заглавных и строчных букв в строке
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case("Hello World!")

# 3. Проверка, является ли строка палиндромом
def is_palindrome(s):
    return s == s[::-1]

print("Is 'radar' a palindrome?", is_palindrome("radar"))  # True
print("Is 'hello' a palindrome?", is_palindrome("hello"))  # False

# 4. Вызов функции квадратного корня после задержки в миллисекундах
def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {number} after {delay} milliseconds is {math.sqrt(number)}")

delayed_sqrt(25100, 2123)

# 5. Проверка, все ли элементы кортежа истинны
values1 = (True, True, False)
values2 = (True, True, True)

print("All elements in values1 are True:", all(values1))  # False
print("All elements in values2 are True:", all(values2))  # True

