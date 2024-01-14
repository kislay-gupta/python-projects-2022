from os import system, name
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import  *
from time import sleep


# import sleep to show output for some time period



# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
money_machine = MoneyMachine()

coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
switch = input("Would like to start the Coffee Make 'yes' or 'no'  ")
if switch == "no":
    is_on = False
else:
    print(beep)
    sleep(2)
    print(boop)
    sleep(2)
    print(start)
    sleep(1)
    print(three)
    sleep(1)
    print(two)
    sleep(1)
    print(one)
    sleep(1)
    print(welcome)
    sleep(1)
clear()
while is_on:
    options = menu.get_items()

    choice = input(f"What would you like? {options} ")
    if choice =="off":
        is_on = False
    elif choice =="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and (money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
