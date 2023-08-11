import os

import art


def addition(number_1, number_2):
    """Returns the sum of two decimal numbers as a float.

    Parameters
    ----------
    number_1 : float
        A float number
    number_2 : float
        Another float number

    Returns
    -------
    float
        A float number
    """
    sum = number_1 + number_2
    return sum


def subtraction(number_1, number_2):
    """Returns the subtraction of two decimal numbers as a float.

    Parameters
    ----------
    number_1 : float
        A float number
    number_2 : float
        Another float number

    Returns
    -------
    float
        A float number
    """
    subtraction = number_1 - number_2
    return subtraction


def multiplication(number_1, number_2):
    """Returns the multiplication of two decimal numbers as a float.

    Parameters
    ----------
    number_1 : float
        A float number
    number_2 : float
        Another float number

    Returns
    -------
    float
        A float number
    """
    multiplication = number_1 * number_2
    return multiplication


def division(number_1, number_2):
    """Returns the division of two decimal numbers as a float.

    Parameters
    ----------
    number_1 : float
        A float number
    number_2 : float
        Another float number

    Returns
    -------
    float
        A float number
    """
    division = number_1 / number_2
    return division


def calculation():
    """Prints the result of the four basic math operations"""
    operations = {"+": addition, "-": subtraction, "*": multiplication, "/": division}
    os.system("cls")
    print(art.logo)

    number_1 = float(input("What's the first number?: "))

    calculation_loop = True
    while calculation_loop:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation: ")
        operation = operations[operation_symbol]
        number_2 = float(input("What's the next number?: "))
        result = operation(number_1, number_2)
        print(f"{number_1} {operation_symbol} {number_2} = {result}")
        continue_calculation = input(
            f"Type 'y' to continue calculating with {result}, of type 'n' to start a new calculation: "
        )
        if continue_calculation == "y":
            number_1 = result
        else:
            calculation_loop = False
            calculation()


calculation()
