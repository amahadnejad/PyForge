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

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

print(isinstance(iterator, Iterator))
print(type(iterator))
print(type(numbers))
print(isinstance(numbers, list))

# ----



























