# Appending new lines

with open("sample.txt", "a") as file:
    file.write("This line was just added.\n")
    file.write("This line was also just added.\n")

print("New lines have been successfully appended.\n")

# Verifying the content

with open("sample.txt", "r") as file:
    content = file.read()

print("Updated file contents:")
print(content)