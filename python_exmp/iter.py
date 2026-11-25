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

def word_generator(str):
    for word in str.split():
        yield word


gen = word_generator("Python Is A PowerFul Language")
for j in gen:
    print(j, end=' - ')

# ----







