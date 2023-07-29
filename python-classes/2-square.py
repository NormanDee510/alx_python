try:
    my_square = Square(3)
    print("Area:", my_square.area())
except TypeError as e:
    print(e)

try:
    my_square = Square(-1)
    print("Area:", my_square.area())
except ValueError as e:
    print(e)