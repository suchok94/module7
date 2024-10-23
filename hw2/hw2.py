from functools import reduce

# task 1
def from_str_to_int(arr: list):
    arr_int = list(map(lambda x: int(x), arr))
    return arr_int


# task 2

def remove_odd_numbers(arr: list):
    new_arr = list(filter(lambda x: x if x % 2 == 0 else False, arr))
    return new_arr

# task 3

def square_list(arr: list):
    new_arr = list(map(lambda x: x**2, arr))
    return new_arr

# task 4

def filter_str_more_3_symbols(arr: list):
    new_arr = list(filter(lambda x: x if len(x) > 3 else False, arr))
    return new_arr

# task 5

def multiply_list(arr: list):
    new_arr = int(reduce(lambda x, y: x * y, arr))
    return new_arr


# task 6

def get_lenght_elements_list(arr: list[str]):
    new_arr = list(map(lambda x: len(x), arr))
    return new_arr

# task 7

def find_longest_word(arr: list):
    new_arr = len(reduce(lambda x,y: x if len(x) > len(y) else y, arr))
    return new_arr

# task 8

def upper_list(arr: list):
    new_arr = list(map(lambda x: x.upper(), arr))
    return new_arr

# task 9

def square_even_numbers(arr: list):
    # new_arr = list(map(lambda x: x**2, list(filter(lambda x: x if x % 2 == 0 else False, list(map(lambda x: int(x), arr))))))
    #new_arr = list(map(lambda x: x ** 2, filter(lambda x: x if x % 2 == 0 else False, map(lambda x: int(x), arr))))
    new_arr = list(map(lambda x: int(x)**2, filter(lambda x: int(x) if int(x) % 2 == 0 else False, arr)))
    return new_arr

# как лучше?

# task 10
def multi_positive_numbers(arr: list):
    new_arr = int(reduce(lambda x,y: x*y, filter(lambda x: x > 0, arr)))
    return new_arr

# task 11

def length_words_start_vowel(arr: list):
    new_arr = list(map(lambda x: len(x), filter(lambda x: x if x[0] in ["a", "e", "i", "o", "u"] else False, arr)))
    return new_arr

# task 12

def filter_polindrome(arr: list):
    new_arr = list(filter(lambda x: x in arr, map(lambda x: x[::-1], arr)))
    return new_arr

# task 13

def multi_even_factorials(arr: list):
    new_arr = int(reduce(lambda x, y: x*y, map(lambda x: fact(x), filter(lambda x: x % 2 == 0, arr))))
    return new_arr


def fact(x):
    if x == 1:
        return 1
    elif x > 1:
        x = x * fact(x-1)
    return x

# ошибка в ответе условия

# task 14

def filter_str_have_even_symbols_upper(arr:list):
    new_arr = ' '.join(map(lambda x: x.upper(), filter(lambda x: len(x)%2 == 0, arr)))
    return new_arr
