# price = {'espresso': 1.5,
#          'latte': 2.5,
#          'cappuccino': 3.0
#          }
resource = {
            'Water': 1000,
            'Milk': 500,
            'Coffee': 76,
            'Money': 2.5
            }
drink = [{'name': 'espresso', 'cost': 1.5, 'Water': 500, 'Coffee': 18, 'Milk': 0},
         {'name': 'latte', 'cost': 2.5, 'water': 200, 'coffee': 24, 'milk': 150},
         {'name': 'cappuccino', 'cost': 3.0, 'water': 250, 'coffee': 24, 'milk': 100}]
# for _ in resource:
#     print(f"{_}: {resource[_]}")

for _ in resource:
    if _ != 'Money':
        resource[_] -= drink[0][_]
print(resource)


# user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
# print(price[user_choice])
#
# quarter = float(input("Please enter the quarters: "))*0.25
# dimes = float(input("Please enter the dimes: "))*0.1
# nickel = float(input("Please enter the nickels: "))*0.05
# penny = float(input("Please enter the pennies: "))*0.01
# money_inserted = quarter + dimes + nickel + penny
#
# if money_inserted >= price[user_choice]:
#     print("Good")
# elif money_inserted < price[user_choice]:
#     print("Sorry that's not enough money. Money refunded.")

# resource = {
#             'Water': 1000,
#             'Milk': 500,
#             'Coffee': 76,
#             'Money': 2.5
#             }
#
# drink = [{'name': 'espresso', 'cost': 1.5, 'water': 50, 'coffee': 18, 'milk': 0},
#          {'name': 'latte', 'cost': 2.5, 'water': 200, 'coffee': 24, 'milk': 150},
#          {'name': 'cappuccino', 'cost': 3.0, 'water': 250, 'coffee': 24, 'milk': 100}]
#
# code = 0
#
# quarter = float(input("Please enter the quarters: "))*0.25
# dimes = float(input("Please enter the dimes: "))*0.1
# nickel = float(input("Please enter the nickels: "))*0.05
# penny = float(input("Please enter the pennies: "))*0.01
# money_inserted = quarter + dimes + nickel + penny
# print(f"Making {drink[code]['name']}")
#
# if money_inserted == drink[code]['cost']:
#     make_drink = True
#     print("Good")
# if money_inserted > drink[code]['cost']:
#     make_drink = True
#     change = money_inserted - drink[code]['cost']
#     print(f"Here is ${change} dollars in change.")
# elif money_inserted < drink[code]['cost']:
#     print("Sorry that's not enough money. Money refunded.")
#
# resource['Water'] -= drink[code]['water']
# resource['Coffee'] -= drink[code]['coffee']
# resource['Milk'] -= drink[code]['milk']
# resource['Money'] += drink[code]['cost']
#
# print(resource)

# money_inserted = 0
# currency = [{'name': 'quarters', 'value': 0.25},
#             {'name': 'dimes', 'value': 0.1},
#             {'name': 'nickels', 'value': 0.05},
#             {'name': 'pennies', 'value': 0.01}]
# for key in range(len(currency)):
#     money_inserted += float(input(f"how many {currency[key]['name']}?: "))*currency[key]['value']
# print(money_inserted)
