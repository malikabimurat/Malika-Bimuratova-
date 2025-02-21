# Generator for squares of numbers up to N
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

# Generator for even numbers between 0 and n
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(",".join(map(str, even_generator(n))))

# Generator for numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Generator yielding squares of numbers from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for sq in squares(2, 6):
    print(sq)

# Generator returning numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
