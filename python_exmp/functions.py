# Tuple Unpacking

def show_info(name, age):
    print(name)
    print(age)


person = ("Amir", 20)

# show_info(*person)

# -------------------


def calculate(a, b):
    print(a + b)


numbers = (50, 25)
# calculate(*numbers)

# -------------------

# List Unpacking


def show_info2(name, age, city):
    print(f"{name} - {age} - {city}")


person2 = ["Reza", "27", "Tabriz"]
# show_info2(*person2)

# -------------------

# Dictionary Unpacking

def show_user(username, email, city):
    print(f"{username} - {email} - {city}")


user = {
    "username": "Hadi",
    "email": "Hado@hadi.com",
    "city": "Mashhad"
}

# show_user(**user)

# -------------------

# Scope of Variables


def calculate2():
    number = 10
    print(number)


# calculate2()

# -------------------

# Local VS Global
name = 'Amir'


def greet():
    print(name)


# greet()
# print(name)

# -> Practice
score = 100


def show_score():
    print(score)


# show_score()
# print(score)

# -------------------

# global Keyword
number = 50


def change_number():
    global number
    number = 200


# change_number()
# print(number)

# -------------------
# Global Vs Local

score = 100


def show_score():
    score = 50
    print(score)


# show_score()
# print(score)

# -------------------
# Scope of Variables

number = 10


def outer():
    number = 20

    def inner():
        number = 30
        print(number)

    inner()


# outer()

# Let's Try Global

number = 10


def change_number():
    global number
    number = 50


# change_number()
# print(number)

# Practice!
score = 100


def update_score():
    global score
    score = 250

update_score()
print(score)


