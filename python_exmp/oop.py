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


# result = MathHelper.multiply(10, 20)
# print(result)
# print(type(result))

# ----

class Book:
    def __init__(self, title):
        self.title = title
        print("Book Object Created!")

    def __del__(self):
        print("Book Object Deleted!")

    def show_title(self):
        print(f"Book: {self.title}")


# book1 = Book('Target')
# book1.show_title()
# del book1


# ----

class Person:
    def introduce(self):
        print("I Am A Person!")


class Student(Person):
    def study(self):
        print('I Am Studying!')


# st1 = Student()
# st1.introduce()
# st1.study()

# ----

class Person:
    def introduce(self):
        print("I am A Person")


class Student(Person):
    def introduce(self):
        print("I am A Student!")


# p1 = Person()
# p1.introduce()

# s1 = Student()
# s1.introduce()

# ----

class Animal:
    def sound(self):
        print("Animal Makes a Sound!")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dogs Says Woof!")


# dog = Dog()
# dog.sound()

# ----

class Father:
    def skills(self):
        print("Father: Driving")


class Mother:
    def talent(self):
        print('Mother: Painting')


class Child(Father, Mother):
    pass


# child = Child()

# child.skills()
# child.talent()

# ----


class Father:
    def show(self):
        print("Father Method")


class Mother:
    def show(self):
        print("Mother Method")


class Child(Father, Mother):
    pass


# child = Child()
# child.show()

# print(Child.__mro__)

# ----

# Polymorphism

class Dog:
    def sound(self):
        print('Woof!')


class Cat:
    def sound(self):
        print("Meow!")

# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()

# ----


class Animal:
    def sound(self):
        print('Animal Makes a Sound!')


class Dog(Animal):
    def sound(self):
        print("Dog Says Woof!")


class Cat(Animal):
    def sound(self):
        print('Cat Says Meow!')


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()

# ----


class Dog:
    def sound(self):
        print("Dog Says Woof!")


class Cat:
    def sound(self):
        print('Cat Says Meow!')


class Cow:
    def sound(self):
        print('Cow Says Moo!')


# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     animal.sound()


# ----

from abc import ABC, abstractmethod

class Animal(ABC):


    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print('Woof!')


class Cat(Animal):

    def make_sound(self):
        print('Meow!')


# dog = Dog()
# cat = Cat()

# dog.make_sound()
# cat.make_sound()

# ----

from abc import ABC, abstractmethod


class Shape(ABC):


    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        print(self.width * self.height)


# rectangle = Rectangle(5, 4)
# rectangle.area()

# ----
# Composition

class Engine:

    def start(self):
        print("Engine Started!")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print('Car Started')


# car = Car()
# car.start_car()

# ----

class Battery:
    def charge(self):
        print("Battery Is Charging!")


class Phone:
    def __init__(self):
        self.battery = Battery()

    def charge_battery(self):
        self.battery.charge()
        print("battery Is Charging.")


# phone = Phone()
# phone.charge_battery()

# ----

class Student:

    def __init__(self, name):
        self.name = name


class University:

    def __init__(self, student):
        self.student = student

    def show_student(self):
        print(self.student.name)


# student1 = Student('Amir')
# university = University(student1)
# university.show_student()

# ----

class Teacher:

    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, teacher):
        self.teacher = teacher

    def show_teacher(self):
        print(self.teacher.name)


# teacher1 = Teacher('Ali')
# school = School(teacher1)
# school.show_teacher()


# ----

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"


# book = Book('Python Programming')
# print(book)

# ----

class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car Brand: {self.brand}"


# car = Car("BMW")
# print(car)

# ----

class Team:
    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


# team = Team(['Ali', 'Amir', 'Reza'])
# print(team)
# print(len(team))

# ----

class Library:
    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)


# books = Library(['The Hobbit', 'Harry Potter', 'The Lord Of The Rings'])
# print(len(books))

# ----





