
from sys import argv

def main():
    args = argv[1:]

    if not args:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(len(args), "s" if len(args) > 1 else ""))
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()