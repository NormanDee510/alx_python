for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num1 == 8 and num2 == 9:
            print("{:01d}{:01d}".format(num1, num2))
        else:
            print("{:01d}{:01d}".format(num1, num2), end=", ")