# Exception Handling

# try:
#     number = int(input("Enter a Number: "))
#     print(number)
#
# except ValueError:
#     print("Please Enter a Valid Number!")


# Multi Error

# try:
#     number = int(input("Enter a Number: "))
#     result = 100 / number
#     print(result)
#
# except ValueError:
#     print("Please Enter a Valid Number")
#
# except ZeroDivisionError:
#     print("Cannot Divide By Zero!")


# else Structure

# try:
#     number = int(input("Enter a Number: "))
#
#
# except:
#     print("Invalid Number!")
#
# else:
#     print("Your Number Is: ", number)

# finally Structure

# try:
#     number = int(input("Enter a Number: "))
#     print(number)
#
# except ValueError:
#     print("Invalid Number!")
#
# finally:
#     print("Program Finished!")

# raise

# score = 10
#
# if score < 0:
#     raise ValueError("Score Cannot Be Negative!")
# else:
#     print(score)

# -- Custom Exceptions
# class NegativeAgeError(Exception):
#     pass
#
#
# age = -2
#
# if age < 0:
#     raise NegativeAgeError("Age Cannot Be Negative!")

# ----


# class InvalidScoreError(Exception):
#     pass
#
#
# score = -10
#
# try:
#     if score < 0:
#         raise InvalidScoreError("Score Cannot Be Negative!")
#
# except InvalidScoreError as error:
#     print(error)

# ----

try:
    number = int(input("Enter a Number: "))
    result = 100 / number

except ValueError:
    print("Please Enter a Valid Number!")

except ZeroDivisionError:
    print("Cannot Divide By Zero!")

else:
    print(result)

