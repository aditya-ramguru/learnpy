from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


money_mach = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

def coffeedispenser(userchoice):
    coffee_type = menu.find_drink(userchoice)
    if coffee_maker.is_resource_sufficient(coffee_type) and money_mach.make_payment(coffee_type.cost):
        coffee_maker.make_coffee(coffee_type)


while True:
    user_choice = input(f"What would you like {Menu().get_items()}: ")
    if user_choice == 'off':
        break
    elif user_choice == 'report':
        coffee_maker.report()
        money_mach.report()
    else:
        coffeedispenser(user_choice)







