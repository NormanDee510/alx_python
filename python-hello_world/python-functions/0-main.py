add = __import__('0-sum').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
# Test case: add(1, 2)
result = add(1, 2)
print(f"Correct output - case: add(1, 2) => {result}")

# Test case: add(100, -2)
result = add(100, -2)
print(f"Correct output - case: add(100, -2) => {result}")

# Test case: add(-100, -2)
result = add(-100, -2)
print(f"Correct output - case: add(-100, -2) => {result}")

# Test case: add(0, 0)
result = add(0, 0)
print(f"Correct output - case: add(0, 0) => {result}")