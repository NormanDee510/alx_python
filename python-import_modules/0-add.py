from add_0 import add

def main():
    a = 1
    b = 2
    result = add(a, b)
    print("FAKE add() => {} - {}".format(a, b))
    print("{:d} + {:d} = {}".format(a, b, result))

    a = 10
    b = 30
    result = add(a, b)
    print("FAKE add() => {} - {}".format(a, b))
    print("{:d} + {:d} = {}".format(a, b, result))

    a = -10
    b = 30
    result = add(a, b)
    print("FAKE add() => {} - {}".format(a, b))
    print("{:d} + {:d} = {}".format(a, b, result))

    a = -10
    b = -30
    result = add(a, b)
    print("FAKE add() => {} - {}".format(a, b))
    print("{:d} + {:d} = {}".format(a, b, result))

if __name__ == "__main__":
    main()