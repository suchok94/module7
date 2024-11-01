# Part 1
# task 1

def generator1(a,b):
    x = a
    while x >= b:
        yield x
        x -= 1

# task 2

def generator2():
    x = 0
    i = 1
    while True:
        if (i + x) % 5 == 0:

            yield i + x
        x = i + x
        if (i + x) % 5 == 0:
            yield i + x
        i = i + x


# task 3
def generator3():
    number = 1
    while True:
        yield fact(number)
        number += 1

def fact(number):
    if number == 0:
        return 1
    elif number > 1:
        number = number * fact(number - 1)
    return number

# task 4

def generator4():
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    while True:
        for i in alphabet:
            yield i

# task 5
def generator5(string):
    string = set(string.split(' '))
    for i in string:
        yield i

# task 6
def generator6(string, number):
    string = string.split()
    string = sorted(list(filter(lambda x: x if len(x) > number else False, string)),reverse=True)
    for i in string:
        yield i
