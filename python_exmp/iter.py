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

# numbers = [10, 20, 30, 40, 50]

# iterator = iter(numbers)

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break


# ----

# numbers = [5, 10, 15, 20, 25]

# iterator = iter(numbers)
# total = 0

# while True:
#     try:
#         current_number = next(iterator)
#         total += current_number
#         print(f'Current Number: {current_number}, total: {total}')
#     except StopIteration:
#         break

# ----

# numbers = [3, 8, 12, 5, 17, 20, 9, 14]
# even_numbers = []

# iterator = iter(numbers)

# while True:
#     try:
#         number = next(iterator)
#         if number % 2 == 0:
#             even_numbers.append(number)
#     except StopIteration:
#         break

# print(even_numbers)

# ----

# numbers = [14, 32, 7, 85, 23, 61, 9]

# iterator = iter(numbers)
# largest = next(iterator)

# while True:
#     try:
#         number = next(iterator)

        # if number > largest:
        #     largest = number

    # except StopIteration:
    #     break

# print(f"Largest Number: {largest}")

# ----


# numbers = [45, 12, 78, 3, 29, 61, 8]

# iterator = iter(numbers)
# lowest = next(iterator)

# while True:
#     try:
#         number = next(iterator)
#         if number < lowest:
#             lowest = number

    # except StopIteration:
    #     break

# print(f"Lowest Number: {lowest}")

# ----

# numbers = [-5, 12, 0, 8, -3, 15, -1, 7]
# count = 0

# iterator = iter(numbers)

# while True:
#     try:
#         number = next(iterator)
#         if number > 0:
#             count += 1

    # except StopIteration:
    #     break

# print(f"Positive Numbers: {count}")

# ----

# words = ["Python", "AI", "Programming", "Code", "Django", "GIT"]
# counts = 0

# iterator = iter(words)

# while True:
#     try:
#         word = next(iterator)
#         if len(word) > 4:
#             counts += 1

    # except StopIteration:
    #     break

# print(f"Counts: {counts}")

# ----

# numbers = [3, 8, 11, 14, 20, 7, 25, 32]
# even_numbers = []

# iterator = iter(numbers)

# while True:
#     try:
#         number = next(iterator)
#         if number % 2 == 0:
#             even_numbers.append(number)

    # except StopIteration:
    #     break

# print(even_numbers)

# ----

# scores = {
#     'Ali': 18,
#     'Sara': 12,
#     'Reza': 20,
#     'Mina': 15,
# }
# passed_students = {}
# iterator = iter(scores.items())

# while True:
#     try:
#         name, score = next(iterator)
#         if score >= 15:
#             passed_students[name] = score

    # except StopIteration:
    #     break

# print(passed_students)

# ----

# words = ['Python', "Django", 'Java', 'HTML', 'Flask']
# iterator = iter(words)
# total_chars = 0

# while True:
#     try:
#         word = next(iterator)
#         total_chars += len(word)
#     except StopIteration:
#         break

# print(f"Total Characters: {total_chars}")

# ----

# def higher(numbers):
#     for number in numbers:
#         if number > 10:
#             yield number


# numbers = [3, 8, 12, 5, 17, 20, 7, 24]
# gen = higher(numbers)

# for number in gen:
#     print(number)

# ----

# def even_numbers(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             yield number


# numbers = [2, 5, 8, 11, 14, 17, 20, 23]

# gen = even_numbers(numbers)

# for i in gen:
#     print(i, end=' ')

# ----

# def square(numbers):
#     for number in numbers:
#         yield number ** 2


# numbers = [2, 3, 4, 5, 6]
# gen = square(numbers)

# for i in gen:
#     print(i, end=" ")

# ----

# def count_up(number):
#     for i in range(1, number + 1):
#         yield i


# gen = count_up(5)
# for i in gen:
#     print(i, end=" ")

# ----

def even_numbers(numbers):
    for number in range(1, numbers + 1):
        if number % 2 == 0:
            yield number


gen = even_numbers(10)
for i in gen:
    print(i, end=" ")









