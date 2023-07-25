from add_0 import add

if __name__ == "__main__":
    def add(a, b):
        return a + b

# Assign values to variables a and b
a = 1
b = 2

# Call the add function and print the result
result = add(a, b)
print("{} + {} = {}".format(a, b, result))

# Print the output with string formatting
print("FAKE add() => {} - {}".format(a, b))