from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. map() to square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# 2. filter() to keep even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 3. reduce() to get sum of all numbers
total = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", total)