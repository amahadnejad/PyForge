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

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


# num1 = Number(10)
# num2 = Number(20)
# old --> print(num1 + num2)
# New Way
# print(num1.__add__(num2))

# ----

class Product:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price


# price1 = 100
# price2 = 250
# print(price1.__add__(price2))

# ----

class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


# p1 = Person(20)
# p2 = Person(20)
# print(p1 == p2)

# ----

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'{self.title}: {self.author}'


# book = Book('The Hobbit', 'Jrr Tolkien')
# print(book)
# print(repr(book))

# ----

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score


# student1 = Student('Amir', 78)
# student2 = Student('Reza', 94)

# print(student1 < student2) # Old Way
# print(student1.__lt__(student2))

# ----

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __le__(self, other):
        return self.price <= other.price


# p1 = Product('Phone', 1250)
# p2 = Product('Laptop', 2510)

# print(p1.__le__(p2))
# print(p1 <= p2)

# ----

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


# car1 = Car('BMW', 120000)
# car2 = Car('Audi', 105000)

# print(car1.__gt__(car2))
# print(car1 > car2)

# ----

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __ge__(self, other):
        return self.score >= other.score


# p1 = Player('John', 54)
# p2 = Player('Mac', 61)

# print(p1 >= p2)

# ----

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def ___ne__(self, other):
        return self.price != other.price


# p1 = Product('Mac', 1000)
# p2 = Product('John', 950)

# print(p1.___ne__(p2))
# print(p1 != p2)

# ----

class Student:
    def __init__(self, students):
        self.students = students

    def __getitem__(self, item):
        return self.students[item]


# students = ['Amir', 'Ali', 'Reza']
# print(students[0])
# print(students[1])

# ----

class Book:
    def __init__(self, books):
        self.books = books

    def __getitem__(self, item):
        return self.books[item]


# books = ['Hobbit', 'LOTR', "Harry Potter"]
# print(books[0])
# print(books[1])

# ----

class ProductList:
    def __init__(self):
        self.items = [10, 20, 30]

    def __setitem__(self, key, value):
        self.items[key] = value


# products = ProductList()
# print(products.items)
# products[0] = 500
# print(products.items)

# ----

class StudentList:
    def __init__(self):
        self.students = ['Amir', 'Reza', 'Ali']

    def __delitem__(self, key):
        del self.students[key]


# students = StudentList()
# print(students.students)
# del students[0]
# print(students.students)

# ----

class ProductList:
    def __init__(self):
        self.products = ['Mouse', 'Laptop', 'Keyboard']

    def __contains__(self, item):
        return item in self.products


# products = ProductList()

# print("Laptop" in products)
# print('Monitor' in products)

# ----

class ProductList:
    def __init__(self):
        self.products = ['Mouse', 'Laptop', 'Keyboard']

    def __iter__(self):
        return iter(self.products)

# p1 = ProductList()

# for item in p1:
#     print(item)

# ----

class BookList:
    def __init__(self):
        self.books = ['Python', 'Django', 'Flask']

    def __iter__(self):
        return iter(self.books)


# books = BookList()
# for book in books:
#     print(book)

# ----

class NumberCounter:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return self.number


counter = NumberCounter()

# print(next(counter))
# print(next(counter))
# print(next(counter))

# ----

class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, name):
        return name in self.members


# team = Team(['Amir', 'Ali', 'Reza'])

# print('Amir' in team)
# print('sara' in team)

# ----

class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return  item in self.books


library = Library(['Hobbit', 'Harry Potter', 'LOTR'])
# print('Hobbit' in library)
# print('The Wizard' in library)

# ----

class User:
    def __init__(self, username, is_active):
        self.username = username
        self.is_active = is_active

    def __bool__(self):
        return self.is_active


# user1 = User('Amir', True)
# user2 = User('Ali', False)
# print(bool(user1))
# print(bool(user2))

# ----

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __call__(self):
        return self.num1 + self.num2


cal = Calculator(10, 20)
print(cal())   # cal.__call()







