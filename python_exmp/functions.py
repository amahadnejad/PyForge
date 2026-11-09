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
show_info2(*person2)












