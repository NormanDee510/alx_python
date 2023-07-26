from add_0 import add

def main():
    
    a = 1
    b = 2
  
    result = add(a, b)
    a = 10
    b = 30
    result = add(a, b)

    a = -10
    b = 30
    result = add(a, b)

    a = -10
    b = -30
    result = add(a, b)
    
    print("FAKE add() => {} - {}".format(a, b))
    print("FAKE add() => {} - {}".format(a, b))
    print("FAKE add() => {} - {}".format(a, b))
    print("FAKE add() => {} - {}".format(a, b))

if __name__ == "__main__":
    main()
