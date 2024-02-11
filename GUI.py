import time
def take_order():
    foods = {
        "Pork Menudo": 60,
        "Pork Siniganag": 60,
        "Munggo Guisado": 30,
        "Kare-kare": 50,
        "Pork Adobo": 50,
        "Humba": 45,
        "Pakbet": 35,
        "Bulalo": 50,
        "Chicken Kalderata": 50,
        "Pansit": 30,
        "Kaldereta": 50,
        "Filipino Pork BBQ": 50,
        "Ginataang hipon": 75,
        "Fried Chicken": 50,
        "Pansit Guisado": 45,
        "Beef mechado": 50,
        "Lumpia": 20,
        "Rice": 10
        
    }

    drinks = {
        "coke": 25,
        "sprite": 25,
        "lemonade": 45,
        "royal": 25,
        "orange juice": 45,
        "iced tea": 39
    }

    order = {}

    print("Welcome to A,J restaurant!")
    print("**************************")
    print("Here our Menu")
    print("Foods:")
    for food, price in foods.items():
        print(f"- {food}: ₱{price}")

    while True:
        food = input("\nEnter a food item (or click [Enter] to finish): ")
        if food == "":
            break
        elif food in foods:
            quantity = int(input("Enter quantity: "))
            print("****Add More Food*****")
            if food in order:
                order[food] += quantity
            else:
                order[food] = quantity
        else:
            print("Invalid food item!")
    print("\nDrinks:")
    for drink, price in drinks.items():
        print(f"- {drink}: ₱{price}")
    while True:
        drink = input("\nEnter a drink item (or click [Enter] to finish): ")
        if drink == "":
            break
        elif drink in drinks:
            quantity = int(input("Enter quantity: "))
            print("****Add More Drinks*****")
            if drink in order:
                order[drink] += quantity
            else:
                order[drink] = quantity
        else:
            print("Invalid drink item!")

    print("Receipt:")
    total_cost = 0
    for item, quantity in order.items():
        if item in foods:
            cost = quantity * foods[item]
        else:
            cost = quantity * drinks[item]
        total_cost += cost
        print(f"{quantity} {item}: ₱{cost:.2f}")

    print(f"\nTotal cost: ₱{total_cost:.2f}")
    print("**********************")
    payment_method = input("Select payment method (1: Cash, 2: GCash): ")
    
    if payment_method == "1":
        cash_received = float(input("Enter cash received: "))
        print("*******************")
        change = cash_received - total_cost
        print(f"Change: {change}")
        goodbye()
    elif payment_method == "2":
        print("Varifying.....")
        time.sleep(5)
        print("Transaction Success")
        time.sleep(2)
        print("Express Send Notifation")
        print(f"You have recieved PHP{total_cost} of Gcash in Ref. NO.0014463926920.")
        goodbye()
    else:
        print("Invalid payment method. Please try again.")

def goodbye():
    print("Thank For Your Ordering")
    print("Come Again")

take_order() 