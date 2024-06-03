resource = {
            'Water': 1000,
            'Milk': 500,
            'Coffee': 76,
            'Money': 0
            }

drink = [{'name': 'espresso', 'cost': 1.5, 'water': 50, 'coffee': 18, 'milk': 0},
         {'name': 'latte', 'cost': 2.5, 'water': 200, 'coffee': 24, 'milk': 150},
         {'name': 'cappuccino', 'cost': 3.0, 'water': 250, 'coffee': 24, 'milk': 100}]

currency = [{'name': 'quarters', 'value': 0.25},
            {'name': 'dimes', 'value': 0.1},
            {'name': 'nickels', 'value': 0.05},
            {'name': 'pennies', 'value': 0.01}]

# drink_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
power = True
stock = False
make_drink = False
money_inserted = 0
code = 0


def stock_check():
    if resource['Water'] < drink[code]['water']:
        print("Sorry there is not enough water. ")
        return False
    elif resource['Coffee'] < drink[code]['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    elif resource['Milk'] < drink[code]['milk']:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def choice_check(choice):
    global code
    if choice == "espresso":
        code = 0
        return code
    elif choice == "latte":
        code = 1
        return code
    elif choice == "cappuccino":
        code = 2
        return code


while power:
    drink_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink_choice == "off":
        break
    elif drink_choice == "report":
        for _ in resource:
            print(f"{_}: {resource[_]}")
            continue
    else:
        code = choice_check(drink_choice)
        stock = stock_check()
    if stock and drink_choice != "report":
        for key in range(len(currency)):
            money_inserted += float(input(f"how many {currency[key]['name']}?: "))*currency[key]['value']

        if money_inserted == drink[code]['cost']:
            make_drink = True
            print("Good")
        if money_inserted > drink[code]['cost']:
            make_drink = True
            change = money_inserted - drink[code]['cost']
            print(f"Here is ${change} dollars in change.")
        elif money_inserted < drink[code]['cost']:
            print("Sorry that's not enough money. Money refunded.")

        if make_drink:
            print("Here is your latte. Enjoy!")
            resource['Water'] -= drink[code]['water']
            resource['Coffee'] -= drink[code]['coffee']
            resource['Milk'] -= drink[code]['milk']
            resource['Money'] += drink[code]['cost']
