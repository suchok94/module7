# task 1
#
# def count_calls(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"Функция 'great' вызвана {count} раз(а)")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @count_calls
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Алексей")
# greet("Мария")
#
# # Вывод:
# # Функция 'greet' вызвана 1 раз(а)
# # Привет, Алексей!
# # Функция 'greet' вызвана 2 раз(а)
# # Привет, Мария!
#


# # task 2
#
# def type_check(func):
#
#     def wrapper(*args, **kwargs):
#
#         for i in args:
#             if not isinstance(i, int):
#                 raise TypeError('Неправильный тип данных')
#
#         for i in kwargs:
#             if not isinstance(i, int):
#                 raise TypeError('Неправильный тип данных')
#
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @type_check
# def add(a, b):
#     return a + b
#
# print(add(2, 3))     # 5
# print(add(2, '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>



# # task 3
# def validate_range(func, min_value=0, max_value=100):
#
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if isinstance(i, int) or isinstance(i, float):
#                 if i >= min_value and i <= max_value:
#                     return func(*args)
#                 raise ValueError(f"Аргумент 'value', имеет значение {i}, что выходит за пределы [{min_value}, {max_value}]")
#
#             else: raise TypeError(f'Не тот формат: {args[i]} = {i}')
#
#         for i in kwargs:
#             if isinstance(i, int) or isinstance(i, float):
#                 if i >= min_value and i <= max_value:
#                     return func(*kwargs)
#                 raise ValueError(f"Аргумент 'value', имеет значение {i}, что выходит за пределы [{min_value}, {max_value}]")
#
#             else: raise TypeError(f'Не тот формат: {kwargs[i]} = {i}')
#
#
#     return wrapper
#
# @validate_range
# def set_percentage(value):
#     print(f"Установлено значение: {value}%")
#
# set_percentage(50)     # Вывод: Установлено значение: 50%
# set_percentage(150)    # ValueError: Аргумент 'value' имеет значение 150, что выходит за пределы [0, 100]


# # task 4
# def trace(func):
#     end = 0
#     def wrapper(*args, **kwargs):
#         nonlocal end
#         end += 1
#         print(f"\t-->Вход в функцию '{func.__name__}' с аргументами {args}, {kwargs}\n", end=end*'\t')
#         result = func(*args, **kwargs)
#         end -= 1
#         print(f"<--Выход из функции '{func.__name__}' с результатом {result}\n", end=end*'\t')
#
#         return result
#
#
#
#     return wrapper
#
#
# @trace
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# factorial(3)
# factorial(6)
# factorial(15)
# # Вывод:
# # --> Вход в функцию 'factorial' с аргументами (3,), {}
# #     --> Вход в функцию 'factorial' с аргументами (2,), {}
# #         --> Вход в функцию 'factorial' с аргументами (1,), {}
# #             --> Вход в функцию 'factorial' с аргументами (0,), {}
# #             <-- Выход из функции 'factorial' с результатом 1
# #         <-- Выход из функции 'factorial' с результатом 1
# #     <-- Выход из функции 'factorial' с результатом 2
# # <-- Выход из функции 'factorial' с результатом 6


# # task 5
# def uppercase_result(func):
#
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             result = result.upper()
#
#         return result
#
#     return wrapper
#
# @uppercase_result
# def get_greeting(name):
#     return f"Привет, {name}"
#
# print(get_greeting("Алексей"))  # Вывод: ПРИВЕТ, АЛЕКСЕЙ
#
# @uppercase_result
# def add_numbers(a, b):
#     return a + b
#
# print(add_numbers(2, 3))  # Вывод: 5


# # task 6
# def call_limit(func, max_calls = 3):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal max_calls
#         nonlocal count
#         if count < max_calls:
#
#             result = func(*args, **kwargs)
#             count += 1
#             return result
#         raise RuntimeError("Превышено максимальное количество вызовов функции")
#
#     return wrapper
#
# @call_limit
# def print_message(msg):
#     print(msg)
#
# print_message("Первый вызов")    # Вывод: Первый вызов
# print_message("Второй вызов")    # Вывод: Второй вызов
# print_message("Третий вызов")    # Вывод: Третий вызов
# print_message("Четвертый вызов") # RuntimeError: Превышено максимальное количество вызовов функции '