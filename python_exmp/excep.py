# Exception Handling

try:
    number = int(input("Enter a Number: "))
    print(number)

except ValueError:
    print("Please Enter a Valid Number!")
