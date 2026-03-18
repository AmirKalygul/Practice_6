names = ["Erali", "Bob", "Amir"]
scores = [85, 90, 95]

# 1. enumerate() to do index + value
print("Using enumerate:")
for index, name in enumerate(names):
    print(index, name)

# 2. zip() to combine lists
print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

# 3. Type checking
x = 10
y = "20"

print("\nType checking:")
print("x is int:", isinstance(x, int))
print("y is str:", isinstance(y, str))

# 4. Type conversion
converted = int(y)  # string → int
result = x + converted

print("\nAfter conversion:")
print("Result:", result)