import csv #comma seperated values

def write_stock():
    with open("stock.csv", "w", newline='') as file: #newline means enter kr diya
        writer = csv.writer(file)
        writer.writerow(["Product", "Quantity", "Price"])

def write_sales():
    with open('sales.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Quantity", "Price", "Customer", "Total"])

def change_stock(product, quantity): #we take the product and search if we have it
    sufficient_stock = True
    with open('stock.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        found_product = False
        for i in rows:
            if i[0] == product:
                found_product = True
                if int(i[1]) >= quantity:
                    i[1] = str(int(i[1]) - quantity) 
                else:
                    sufficient_stock = False  
                break
        
        
        if not found_product:
            sufficient_stock = False
    
    
    with open('stock.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    return sufficient_stock

def enter_new_stock():
    product = input("Enter product name : ")
    quantity = input("Enter the quantity : ")
    price = int(input("Enter the price : "))
    with open('stock.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product, quantity, price])
    print("New stock added successfully!")


def add_sales():
    product = input("Enter the product: ")
    quantity = int(input("Enter the quantity: "))
    customer = input("Enter Customer name: ")

    sufficient_stock = change_stock(product, quantity)
    if not sufficient_stock:
        print("Insufficient stock. Sale not recorded.")
        return

    price = 0
    with open('stock.csv', 'r') as file: #openned stock csv file in read mode
        reader = csv.reader(file)
        for i in reader:
            if i[0] == product:
                price = int(i[2])
                break

    total_price = price * quantity

    with open("sales.csv", "a", newline="") as file: #a means append which means ki last me neter kra h
        writer = csv.writer(file)
        writer.writerow([product, quantity, price, customer, total_price])
    print("Sale recorded successfully!")


def print_stock():
    with open('stock.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def print_sales():
    with open('sales.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

write_sales()
write_stock()
while True:
        print("\nElectronic Store Management System")
        print("1. Add new sales")
        print("2. Update stock")
        print("3. Print sales till now")
        print("4. Print current stock")
        print("5. Add Stock")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_sales()
        elif choice == '2':
            change_stock()
        elif choice == '3':
            print_sales()
        elif choice == '4':
            print_stock()
        elif choice == '5':
            enter_new_stock()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")
