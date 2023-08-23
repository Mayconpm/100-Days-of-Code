from os import system

from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

system("cls")

money = 0
machine_working = True

while machine_working:
    ingredients_sufficient = None
    payment = None
    drinks = menu.get_items().rstrip("/")
    selected_drink = input(f"What would you like? ({drinks}):")

    if selected_drink == "report":
        coffee_maker.report()
        money_machine.report()
        selected_drink = None
    elif selected_drink == "off":
        machine_working = False
        selected_drink = None
    else:
        selected_drink = menu.find_drink(selected_drink)

    if selected_drink:
        ingredients_sufficient = coffee_maker.is_resource_sufficient(selected_drink)

    if ingredients_sufficient:
        payment = money_machine.make_payment(selected_drink.cost)

    if payment:
        coffee_maker.make_coffee(selected_drink)
