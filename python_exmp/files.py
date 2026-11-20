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

# with open('files/data.txt', 'r') as file:
#     content = file.readlines()
#     print(content)

# ----

# with open('files/data.txt', 'r') as file:
#     for line in file:
#         print(line)

# ----

# with open('files/data.txt', 'a') as file:
#     file.write('\nFlask')

# ----

# with open('files/data.txt') as file:
#     file.seek(6)
#     content = file.read()
#     print(content)

# ----

# with open('files/data.txt', 'r') as file:
#     print(file.tell())
#     file.read(10)
#     print(file.tell())

# ----

# with open('files/data.txt', 'r') as file:
#     content = file.readline()
#     print(content)
#     content = file.readline()
#     print(content)

# ----

# with open('files/data.txt', 'r') as file:
#     content = file.readlines()
#     print(content)

# ----

# languages = ['Python\n', 'JavaScripts\n', 'Django\n']

# with open("files/data.txt", 'w') as file:
#     file.writelines(languages)

# ----

# with open('files/data.txt', 'w') as file:
#     file.write('Learning Python Is Fun')
#     file.flush()
#     print(file.closed)

# print(file.closed)

# ----

# with open("files/data.txt", 'r') as file:
#     file.seek(9)
#     content = file.read(7)
#     print(content)

# ----

with open('files/data.txt', 'r+') as file:
    file.seek(7)
    file.truncate()

    file.seek(0)
    content = file.read()
    print(content)













