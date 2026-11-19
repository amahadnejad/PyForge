# Files Handling

# file = open('files/1.txt', 'w')
# file.write('Hello World!')
# file.close()

# ----

# file = open('files/pyforge.txt', 'w')
# file.write("Welcome To PyForge!\nI Am Learning Python File Handling")
# file.close()

# ----

# file = open('files/data.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# ----

# with open('files/data.txt', 'r') as file:
#     content = file.read()
#     print(content)

# ----

# with open('files/data.txt', 'r') as file:
#     content = file.read()
#     print(content)

# ----

# with open('files/data.txt', 'r') as file:
#     line1 = file.readline()
#     print(line1)

# ----

with open('files/data.txt', 'r') as file:
    content = file.readlines()
    print(content)







