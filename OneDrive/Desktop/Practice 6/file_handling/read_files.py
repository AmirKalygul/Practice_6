# Creating a sample text

with open("sample.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the last line (for now).\n")

print("File created and data written.\n")

# Reading and printing file contents

with open("sample.txt", "r") as file:
    content = file.read()

print("File contents:")
print(content)