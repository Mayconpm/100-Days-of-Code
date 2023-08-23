from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def generate_report(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\n Milk: {milk}ml \n Coffee: {coffee}g"


def calculate_resources(beverage):
    ingredients = beverage["ingredients"]
    resources_temp = resources.copy()
    for ingredient, value in ingredients.items():
        resources_temp[ingredient] -= value
        if resources_temp[ingredient] < 0:
            print(f"Sorry there is not enough {ingredient}.")
            return None
    else:
        return resources_temp


def process_coins():
    coins_value = 0
    coins = {"quarter": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    for coin, value in coins.items():
        coins_value += int(input(f"how many {coin}?: ")) * value
    return coins_value


machine_working = True
money = 0
system("cls")
while machine_working:
    selected_drink = input("What would you like? (espresso/latte/cappuccino):")
    if selected_drink == "off":
        machine_working = False
    elif selected_drink == "report":
        print(f"{generate_report(resources)}\n Money: ${money}")
    else:
        drink = MENU[selected_drink]
        resources_temp = calculate_resources(drink)
        if resources_temp:
            coins_value = process_coins()
            drink_cost = drink["cost"]
            change = coins_value - drink_cost
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change :.2f} in change.")
                money += drink_cost
                resources = resources_temp
                print(f"Here is your {selected_drink}☕️. Enjoy!")
