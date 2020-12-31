from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

register = MoneyMachine()
mr_coffee = CoffeeMaker()
menu = Menu()

power_on = True


while power_on is True:
    bypass_mode = False
    options = menu.get_items()
    user_choice = str(input(f"What would you like: ({options})?: "))

    if user_choice == "off":
        bypass_mode = True
        power_on = False
        print("Powering down.")
    elif user_choice == "report":
        register.report()
        mr_coffee.report()
    else:
        drink = menu.find_drink(user_choice)

        if mr_coffee.is_resource_sufficient(drink) is True:
            if register.make_payment(drink.cost) is True:
                mr_coffee.make_coffee(drink)

        # check resources
        # ask for money
        # return change


