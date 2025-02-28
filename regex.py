import re

# 1. Найти строку, содержащую 'a' с нулем или более 'b'
def match_ab_zero_or_more(s):
    return bool(re.fullmatch(r'ab*', s))

# 2. Найти строку, содержащую 'a' с двумя или тремя 'b'
def match_ab_two_to_three(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

# 3. Найти последовательности строчных букв, соединенных с подчеркиванием
def find_lowercase_with_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

# 4. Найти последовательности одной заглавной буквы, за которой идут строчные
def find_capital_followed_by_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

# 5. Найти строку, начинающуюся на 'a', затем любые символы, заканчивающуюся на 'b'
def match_a_anything_b(s):
    return bool(re.fullmatch(r'a.*b', s))

# 6. Заменить пробелы, запятые и точки на двоеточие
def replace_space_comma_dot(s):
    return re.sub(r'[ ,.]', ':', s)

# 7. Преобразовать snake_case в CamelCase
def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))

# 8. Разделить строку по заглавным буквам
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

# 9. Вставить пробелы между словами, начинающимися с заглавных букв
def insert_spaces_between_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

# 10. Преобразовать CamelCase в snake_case
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

# Тестовые примеры
print(match_ab_zero_or_more("abbb"))  # True
print(match_ab_two_to_three("abb"))  # True
print(find_lowercase_with_underscore("hello_world test_case"))  # ['hello_world', 'test_case']
print(find_capital_followed_by_lower("Hello World Test"))  # ['Hello', 'World', 'Test']
print(match_a_anything_b("a123b"))  # True
print(replace_space_comma_dot("Hello, world. This is a test"))  # "Hello:world:This:is:a:test"
print(snake_to_camel("hello_world_test"))  # "HelloWorldTest"
print(split_at_uppercase("HelloWorldTest"))  # ['', 'Hello', 'World', 'Test']
print(insert_spaces_between_capitals("HelloWorldTest"))  # "Hello World Test"
print(camel_to_snake("HelloWorldTest"))  # "hello_world_test"
