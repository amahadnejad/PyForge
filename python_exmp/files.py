# Files Handling

# file = open('files/1.txt', 'w')
# file.write('Hello World!')
# file.close()

# ----

# file = open('files/pyforge.txt', 'w')
# file.write("Welcome To PyForge!\nI Am Learning Python File Handling")
# file.close()

# ----

file = open('files/data.txt', 'r')
content = file.read()

print(content)
file.close()
