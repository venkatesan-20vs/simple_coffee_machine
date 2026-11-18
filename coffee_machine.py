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

profit = 0

def resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True

def coins():
    print("Insert you coins")
    quarters = int(input("How many quarters?"))* 0.25
    dimes = int(input("How many dimes?"))* 0.1
    nickles = int(input("How many nickles?"))* 0.05
    pennies = int(input("How many pennies?"))* 0.01
    total = quarters + dimes + nickles + pennies
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit = profit + drink_cost
        change = round(money_received - drink_cost,2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry that's not enough money,Money refunded")
        return False


coffee_machine = True

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

while coffee_machine:
    choice = input("What would you like? (espresso/latte/capuccino):").lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    elif choice == "off":
        print("Bye")
        coffee_machine = False
    else:
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


