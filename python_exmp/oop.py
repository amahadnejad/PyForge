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


# book1 = Book('The Stranger', 'Albert Camus')
# book1.show_info()

# ----

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self):
        self.score += 1
        print(f"1 Score Granted! scores:{self.score}")


# player1 = Player('Mac', 25)
# player1.add_score()

# ----

class Car:
    def __init__(self, brand):
        self.brand = brand

    def change_brand(self, new_brand):
        self.brand = new_brand


# car1 = Car('BMW')
# car2 = Car('Benz')

# print(car1.brand)
# print(car2.brand)

# ----

class Employee:
    company = 'google'

    def __init__(self, name):
        self.name = name


# emp1 = Employee('John')
# emp2 = Employee('Max')

# print(f'{emp1.name} at {emp1.company}')
# print(f'{emp2.name} at {emp2.company}')

# ----

class Car:
    brand = "Toyota"


# car1 = Car()
# car2 = Car()

# car1.brand = 'BMW'
# print(car1.brand)
# print(car2.brand)

# ----

class Phone:
    brand = 'Samsung'


# phone1 = Phone()
# phone2 = Phone()

# Phone.brand = "Apple"

# print(phone1.brand)
# print(phone2.brand)

# ----

class Student:
    school = "Python Academy"

    def show_school(self):
        print(self.school)


# stu1 = Student()
# stu2 = Student()

# stu1.show_school()
# stu2.show_school()

# ----

class Book:
    category = 'Programming'

    def show_category(self):
        print(Book.category)


# book1 = Book()
# book2 = Book()

# book1.show_category()
# book2.show_category()

# ----


# class University:
#     name = 'Oxford'
#
#     @classmethod
#     def show_name(cls):
#         print(cls.name)

# University.show_name()

# ----

class Employee:
    company = 'Google'

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Employee: {self.name}")

    def show_company(cls):
        print(f"Company: {cls.company}")


# emp1 = Employee('Amir')
# emp1.show_name()
# emp1.show_company()

# ----

class MathHelper:

    @staticmethod
    def multiply(a, b):
        return a * b


result = MathHelper.multiply(10, 20)
print(result)
print(type(result))




























