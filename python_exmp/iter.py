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

def square_numbers(number):
    for i in range(1, number + 1):
        yield i ** 2


gen = square_numbers(5)

for j in gen:
    print(j, end=' ')

















