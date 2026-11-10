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

try:
    number = int(input("Enter a Number: "))


except:
    print("Invalid Number!")

else:
    print("Your Number Is: ", number)

