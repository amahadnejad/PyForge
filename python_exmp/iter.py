"""
    Second Iterator & Generator Practice
"""


# def even_numbers():
#     for i in range(1, 21):
#         if i % 2 == 0:
#             yield i


# gen = even_numbers()

# for i in gen:
#     print(i, end=' ')

# ----

# def square_numbers(number):
#     for i in range(1, number + 1):
#         yield i ** 2


# gen = square_numbers(5)

# for j in gen:
#     print(j, end=' ')

# ----

# def filter_numbers(number):
#     for i in range(1, number + 1):
#         if i % 3 == 0:
#             yield i


# gen = filter_numbers(30)

# for j in gen:
#     print(j, end=' ,')

# ----

# def filter_even_numbers(number):
#     for i in range(1, number + 1):
#         if i % 2 == 0 and i % 3 == 0:
#             yield i


# gen = filter_even_numbers(35)
# for j in gen:
#     print(j, end=' ')

# ----

# def characters(string):
#     for i in string:
#         yield i


# gen = characters('Hello Python!')

# for j in gen:
#     print(j, end=" ")

# ----

# def word_generator(str):
#     for word in str.split():
#         yield word


# gen = word_generator("Python Is A PowerFul Language")
# for j in gen:
#     print(j, end=' - ')

# ----

# def number_analyzer(number):
#     for i in range(1, number + 1):
#         if i % 2 == 0:
#             yield i ** 2


# gen = number_analyzer(10)

# for j in gen:
#     print(j, end=' ')

# ----

# product = {
#     'name': 'LapTop',
#     'Price': 1500,
#     'brand': 'Asus'
# }

# iterator = iter(product)
# for key in iterator:
#     print(key)

# ----

# student = {
#     'name': 'Amir',
#     'age': 20,
#     'grade': 18,
# }

# iterator = iter(student.items())

# while True:
#     try:
#         key, value = next(iterator)
#         print(f"{key}: {value}")

    # except StopIteration:
    #     break

# ----

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


# ----











