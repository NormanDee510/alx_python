from add_0 import add

def main():
    a = 1
    b = 2
    result = add(a, b)
    print(" a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

    a = 10
    b = 30
    result = add(a, b)
    print("a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

    a = -10
    b = 30
    result = add(a, b)
    print(" a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

    a = -10
    b = -30
    result = add(a, b)
    print("a = {} and b = {} FAKE add() => {} - {}".format(a, b, a, b))

if __name__ == "__main__":
    main()
