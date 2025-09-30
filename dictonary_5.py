products = {}
# products = {'kiwi': {'qty': 30, 'price': 700}, 'apple': {'qty': 40, 'price': 49}}

menu = """
        press 1 for manager
        press 2 for curstomer
        press 3 for exit
"""
status = True
while status:
    subdictionary = {}
    print(menu)
    choice = int(input("enter your choice : "))
    
    if choice==1:
        print("WELCOME TO MANAGER PANEL")
        name = input("Enter product name : ")
        qty = int(input("enter product qauntity : "))
        price = int(input("enter price : "))
        if name in products.keys():
            subdictionary["qty"] = products[name]["qty"] + qty
            subdictionary["price"] = price
        else:
            subdictionary["qty"]=qty
            subdictionary["price"]=price
        products[name] = subdictionary
        
        print(products)
    elif choice==2:
        print("\nAvailable Products:")
        for k, v in products.items():
            print(f"{k}\t qty: {v['qty']} boxes \t price per box: Rs. {v['price']}")

        p_name = input("Enter product you want to buy : ")

        if p_name not in products:
            print("Product not available.")
            continue

        p_qt = int(input("Enter quantity you want to purchase : "))

        if p_qt > products[p_name]["qty"]:
            print("Sorry, not enough stock available.")
            continue

        price = p_qt * products[p_name]["price"]
        print("Total price = Rs.", price)

        confirm = input("Do you want to proceed? (y/n): ")
        if confirm.lower() == "y":
            products[p_name]["qty"] -= p_qt
            print("Thank you for shopping!")
            print("Updated stock:", products)
        else:
            print("Purchase cancelled.")

    elif choice == 3:
        print("Goodbye!")
        status = False
    else:
        print("Invalid choice, try again!")

# {'kiwi': {'qty': 30, 'price': 700}, 'apple': {'qty': 40, 'price': 49}}