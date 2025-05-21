MENU = {
    "espresso" : {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee" : 18,
        },
        "cost" : 1.50
    },
    "latte" : {
        "ingredients": {
            "water": 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.50
    },
    "cappuccino" : {
        "ingredients": {
            "water": 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.00
    }
}

resources = {
    "water": 300,
    "milk" : 200,
    "coffee" : 100,
    "profit" : 0,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    # returns total money inserted
    print("Please insert coins(pennies/nickles/dimes/quarters): ")
    total = (0.01)*int(input("pennies: "))
    total += (0.05)*int(input("nickles: "))
    total += (0.10)*int(input("dimes: "))
    total += (0.25)*int(input("quarters: "))
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved<drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_recieved>=drink_cost:
        resources["profit"] += drink_cost
        return True
        
is_on = True

while is_on:
    type = input("What would you like? (espresso/latte/cappuccino): ")
    if type=="off":
        is_on = False
    
    elif type=="report":
        print(resources)

    else:
        drink = MENU[type]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]

                if payment>drink["cost"]:
                    change = round(payment - drink["cost"], 2)
                    print(f"Here is {change} dollars in change")

                print(f"Here is your {type} ☕. Enjoy!")

            