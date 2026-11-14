# Object_oriented Programming (OOP)

# Class

# class Car:
#     brand = "BMW"
#     color = "Black"


# my_car = Car()

# print(my_car.brand)
# print(my_car.color)

# ----
#
# class Student:
#     name = "Amir"
#     age = "25"


# student1 = Student()

# print(student1.name)
# print(student1.age)

# ----

# class Car:
#     brand = "Benz"


# car1 = Car()
# car2 = Car()

# print(car1.brand)
# print(car2.brand)

# ----

# class Car:
#     brand = "Benz"


# car1 = Car()
# car2 = Car()

# car1.brand = "Toyota"
# car2.brand = "Porsche"

# print(car1.brand)
# print(car2.brand)

# ----

class Car:
    brand = "Benz"

    def start(self):
        print("Car Started!")


# car1 = Car()

# car1.start()

# ----

class Dog:
    def bark(self):
        print("Woof Woof!")


# dog1 = Dog()
# dog1.bark()

# ----

# class Dog:
#     def bark(self):
#         print(f"{self.name} Says Woof!")
#
#
# dog1 = Dog()
# dog1.name = "Max"
# dog1.bark()


class Person:
    def introduce(self):
        print(f"Hi I'm {self.name}")


# person1 = Person()
# person1.name = "John"
# person1.introduce()


# ----

class Person:
    def __init__(self, name):
        self.name = name


# person1 = Person("Amir")
# print(person1.name)

# ----

class Car:
    def __init__(self, brand):
        self.brand = brand


# car1 = Car('BMW')
# print(car1.brand)

# ----

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# student1 = Student("Brad", 25)
# print(f"{student1.name} : {student1.age}")

# ----

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f'{self.title} by {self.author}')


book1 = Book('The Stranger', 'Albert Camus')

book1.show_info()






