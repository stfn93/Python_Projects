from cs50 import get_int


def main():

    while True:
        height = get_int("Height: ")
        if height > 0 and height < 9:
            break

    for i in range(height):
        print_space(i, height)     # Call the print_space function
        print_sign(i)              # Call the print_sign function
        print()


def print_space(i, height):
    # Print spaces before the # symbols
    print(" " * (height - i - 1), end="")


def print_sign(i):
    # Print # symbols
    print("#" * (i + 1), end="")


main()
