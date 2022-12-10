import qrcode


def readFromDatabase():
    print("Loading ...")
    file = open("Database.txt", "r")

    for line in file:
        tempProduct = line[:-1].split(",")
        newProduct = {"code":tempProduct[0], "name":tempProduct[1], "price":tempProduct[2], "count":tempProduct[3]}
        PRODUCTS.append(newProduct)
    
    file.close()
    print("Database loaded.")


def menu():
    print("1. Add")
    print("2. Edit")
    print("3. Remove")
    print("4. Search")
    print("5. Show list")
    print("6. Buy")
    print("7. Make QR code")
    print("8. Exit")

    menuChoice = int(input("Enter your choice --> "))
    return menuChoice


def add():
    tempCode = input("\nEnter a code for product: ")
    tempName = input("Enter a name for product: ")
    tempPrice = input("Enter a price for product: ")
    tempCount = input("Enter number of the product: ")

    newProduct = {"code":tempCode, "name":tempName, "price":tempPrice, "count":tempCount}
    
    if not any(product["code"] == tempCode for product in PRODUCTS):
        PRODUCTS.append(newProduct)
        print("\ncode\tname\tprice\tcount".expandtabs(12))
        print(f"{newProduct['code']}\t{newProduct['name']}\t{newProduct['price']}\t{newProduct['count']}".expandtabs(12))
    else:
        print("\nThis product is already available.")


def edit():
    showList()
    code = input("\nEnter a product code you want to edit: ")
    
    for product in PRODUCTS:
        if product["code"] == code:
            print("code\tname\tprice\tcount".expandtabs(12))
            print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))

            print("\nWhich parts do you want to edit? ")
            print("1. Name")
            print("2. Price")
            print("3. Count")
            editChoice = int(input("--> "))
            
            if editChoice == 1:
                product["name"] = input("Enter a name: ")
                print("\nInformation updated successfully!")
                print("code\tname\tprice\tcount".expandtabs(12))
                print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
                break
            elif editChoice == 2:
                product["price"] = input("Enter a price: ")
                print("\nInformation updated successfully!")
                print("code\tname\tprice\tcount".expandtabs(12))
                print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
                break
            elif editChoice == 3:
                product["count"] = input("Enter number of the product: ")
                print("\nInformation updated successfully!")
                print("code\tname\tprice\tcount".expandtabs(12))
                print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
                break
            else:
                print("\nThat's wrong! Try again.")
                break
    else:
        print("\nThe product was NOT found to edit.") 


def remove():
    showList()
    code = input("\nEnter a product code you want to remove: ")

    for product in PRODUCTS:
        if product["code"] == code:
            print("code\tname\tprice\tcount".expandtabs(12))
            print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))

            removeChoice = input("Are you sure? y/n ").lower()

            if removeChoice == "y":
                PRODUCTS.remove(product)
                showList()
                print("\nYour product has been removed successfully!")
                break
            elif removeChoice == "n":
                break
            else:
                print("\nYour request has not been defined!")
                break
    else:
        print("\nThe product was NOT found to remove.")


def search():
    searchInput = input("\nEnter a product code or its name you want: ")
    
    for product in PRODUCTS:
        if product["code"] == searchInput or product["name"] == searchInput:
            print("\nThe product was found.")
            print("code\tname\tprice\tcount".expandtabs(12))
            print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))
            break 
    else:
        print("\nThe product was NOT found.")


def showList():
    print("code\tname\tprice\tcount".expandtabs(12))

    for product in PRODUCTS:
        print(f"{product['code']}\t{product['name']}\t{product['price']}\t{product['count']}".expandtabs(12))


def buy():
    showList()
    shoppingBasket = []
    sumPrice = 0

    while True:
        code = input("\nWhich items do you want to buy? Enter its code one by one: ")

        for product in PRODUCTS:
            if product["code"] == code:
                number = int(input("How many do you need? "))

                if number <= int(product["count"]):
                    sumPrice = sumPrice + (number * int(product["price"]))
                    newItem =  {"code":product["code"], "name":product["name"], "price":product["price"], "count":number}

                    for item in shoppingBasket:
                        if code == item["code"]:
                            item["count"] = str(int(item["count"]) + number)
                            break    
                    else:
                        shoppingBasket.append(newItem)

                    product["count"] = str(int(product["count"]) - number)
                    
                    if int(product["count"]) == 0:
                        PRODUCTS.remove(product)
                    break
                else:
                    print("\nThis number of the product is NOT available.")
                    break
        else:
            print("\nThe product was NOT found.")

        buyChoice = input("Do you wanna continue? y/n ").lower()

        if buyChoice == "n":
            if sumPrice != 0:
                print("\nYour Bill:")
                print("code\tname\tprice\tcount\ttotal".expandtabs(12))

                for item in shoppingBasket:
                    print(f"{item['code']}\t{item['name']}\t{item['price']}\t{item['count']}\t{int(item['price']) * int(item['count'])}".expandtabs(12))
                print("Total amount =", sumPrice)
                break
            else:
                break
        elif buyChoice == "y":
            continue
        else:
            print("\nYour request has not been defined!")
            break


def infoToQRcode():
    code = input("\nEnter a product code you want: ")

    for product in PRODUCTS:
        if product["code"] == code:
            image = qrcode.make(f"Code: {product['code']} | Name: {product['name']} | Price: {product['price']} | Count: {product['count']}")
            image.save(f"{product['code']}_{product['name']}.jpg")
            print("\nQR code was made successfully!")
            break
    else:
        print("The product was NOT found.")
    
            
def writeToDatabase():
    try:
        file = open("Database.txt", "w")
        for product in PRODUCTS:
            file.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")
        file.close()
    except IOError:
        print("I/O error")
  

PRODUCTS = []

readFromDatabase()
print("\nWelcome to Mahtab Store")

while True:
    print()
    choice = menu()

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        showList()     
    elif choice == 6:
        buy()
    elif choice == 7:
        infoToQRcode()
    elif choice == 8:
        writeToDatabase()
        exit()
    else:
        print("\nThe input isn't valid.\nTry again!")