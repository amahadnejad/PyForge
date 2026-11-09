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


calculate2()



