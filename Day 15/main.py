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
    resources_temp = resources
    for ingredient, value in ingredients.items():
        resources[ingredient] -= value
        if resources[ingredient] < 0:
            print()
            return resources
    else:
        return resources_temp


machine_working = True
money = 0

while machine_working:
    drink = input("What would you like? (espresso/latte/cappuccino):")
    if drink == "report":
        print(f"{generate_report(resources)}")
    else:
        resources = calculate_resources(MENU[drink])
