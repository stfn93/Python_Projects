from cs50 import get_float


def main():

    while True:
        cents = get_float("Change owed: ")
        if cents > 0:
            break

    cents = round(cents * 100)
    # Calculate how many quarters you should give customer
    quarters = calculate_quarters(cents)

    # Subtract the value of those quarters from cents
    cents = cents - (quarters * 25)

    # Calculate how many dimes you should give customer
    dimes = calculate_dimes(cents)

    # Subtract the value of those quarters from cents
    cents = cents - (dimes * 10)

    # Calculate how many dimes you should give customer
    nickles = calculate_nickles(cents)

    # Subtract the value of those nickles from cents
    cents = cents - (nickles * 5)

    # Calculate how many pennies you should give customer
    pennies = calculate_pennies(cents)

    # Subtract the value of those quarters from cents
    cents = cents - (pennies * 1)

    coins = quarters+dimes+nickles+pennies

    print(coins)


def calculate_quarters(cents):

    # Calculate how many quarters you should give customer
    quarters = 0
    while cents >= 25:
        quarters += 1
        cents = cents - 25
    return quarters


def calculate_dimes(cents):

    # Calculate how many dimes you should give customer
    dimes = 0
    while cents >= 10:
        dimes += 1
        cents = cents - 10
    return dimes


def calculate_nickles(cents):

    # Calculate how many nickles you should give customer
    nickles = 0
    while cents >= 5:
        nickles += 1
        cents = cents - 5
    return nickles


def calculate_pennies(cents):

    # Calculate how many pennies you should give customer
    pennies = 0
    while cents >= 1:
        pennies += 1
        cents = cents - 1
    return pennies


main()
