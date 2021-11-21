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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def is_resource_sufficient(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"sorry not enough {item}")
            return False
    return True


def process_coins():
    print("Enter coins")
    total = int(input('Enter no of quarters: '))*0.25
    total += int(input("Enter no of dimes: "))*0.10
    total += int(input("Enter no of nickles: "))*0.05
    total += int(input("Enter no of pennies: "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"here is ${change} in change.")
        return True
    else:
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"here is your {drink_name}.Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report()
    else:
        drink = MENU[choice]
        is_resource_sufficient(drink['ingredients'])
        payment = process_coins()
        if is_transaction_successful(payment, drink['cost']):
            make_coffee(choice, drink["ingredients"])
