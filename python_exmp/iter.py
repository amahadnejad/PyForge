"""
    --> Iterator & Generator
"""

# numbers = [10, 20, 30, 40]
# my_iterator = iter(numbers)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# ----

# fruits = ['Apple', 'Banana', 'Orange']
# my_iterator = iter(fruits)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# ----

# colors = ['Red', 'Green', 'Blue']
# my_iterator = iter(colors)

# try:
#     print(next(my_iterator))
#     print(next(my_iterator))
#     print(next(my_iterator))
#     print(next(my_iterator))
# except StopIteration:
#     print("Iterator Is Finished!")

# ----

# languages = ['Python', 'java', 'JavaScript', 'PHP']
# my_iterator = iter(languages)

# while True:
#     try:
#         item = next(my_iterator)
#         print(item)
#     except StopIteration:
#         break

# ----

# fruits = ['Apple', 'Banana', 'Coconut']

# iterator = iter(fruits)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# ----
from collections.abc import Iterator

# numbers = [10, 20, 30]

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# print(isinstance(iterator, Iterator))
# print(type(iterator))
# print(type(numbers))
# print(isinstance(numbers, list))

# ----

# colors = ['Red', 'Blue', 'Green']

# iterator = iter(colors)

# for color in iterator:
#     print(color)

# ----

# language = 'Django'

# iterator = iter(language)

# for letter in iterator:
#     print(letter)

# ----

# cities = ('Tehran', 'Seattle', 'New York')

# iterator = iter(cities)

# for city in iterator:
#     print(city)

# ----

# programming = {'Python', 'Java', 'PHP'}

# iterator = iter(programming)

# for lang in iterator:
#     print(lang)

# ----

# student = {
#     'name': 'Amir',
#     'age': 25,
#     'language': 'Persian',
# }

# iterator = iter(student.items())

# for item in iterator:
#     print(item)

# ----

# Generators


# def count_number():
#     yield 10
#     yield 20
#     yield 30


# for number in count_number():
#     print(number)

# ----

# def my_gen():
#     for number in range(1, 6):
#         yield number


# for item in my_gen():
#     print(item)

# ----


def even_number():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i


for number in even_number():
    print(number)











