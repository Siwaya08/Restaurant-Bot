import time 

print("Welcome to our restaurant, what would you like today")

while True:
    try:
        choice = int(input("Enter 1 for veg and 2 for non-veg: "))
        if choice in [1, 2]:
            break  
        print("Invalid choice! Please enter either 1 or 2.")
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")

vegm = [100, 60, 40]
nvegm = [120, 100, 110]
numitem = 0
total = 0

if choice == 1:
    print("\nVeg menu\nChole Bhature-100\nAloo tiki-60\nBhel chaat-40")
    
    while True:
        try:
            numitem = int(input("Enter num of items you would like to select: "))
            if numitem >= 0:
                break
            print("Please enter a valid number of items (0 or more).")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            
    while numitem > 0:
        while True:
            try:
                order = int(input("\n0 for Chole Bhature-100 \n1 for Aloo tiki-60\n2 for Bhel chaat-40\nYour choice: "))
                if order in [0, 1, 2]:
                    break
                print("Invalid item! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        total = vegm[order] + total
        print("Current total is", total)
        numitem = numitem - 1

elif choice == 2:
    print("\nNon-veg menu \nTandori chicken-120\nChicken roll-100\nFish fry-110")
    
    while True:
        try:
            numitem = int(input("Enter num of items you would like to select: "))
            if numitem >= 0:
                break
            print("Please enter a valid number of items (0 or more).")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            
    while numitem > 0:
        while True:
            try:
                order = int(input("\n0 for Tandori chicken-120\n1 for Chicken roll-100\n2 for Fish fry-110\nYour choice: "))
                if order in [0, 1, 2]:
                    break
                print("Invalid item! Please enter 0, 1, or 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")
                
        total = nvegm[order] + total
        print("Current total is", total)
        numitem = numitem - 1

if total > 0:
    print(f"\nYour final total is: {total}")
    while True:
        try:
            payment = int(input("How would you like to pay? 1 for UPI, 2 for Card, 3 for Cash: "))
            if payment in [1, 2, 3]:
                break
            print("Invalid option! Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    if payment == 1:
        print("Redirecting to UPI gateway...")
        time.sleep(2)
        print("Payment received!")
    elif payment == 2:
        print("Enter your card PIN...")
        time.sleep(2)
        print("Redirecting...")
        time.sleep(1)
        print("Payment received!")
    elif payment == 3:
        print("Please hand the staff your cash.")
else:
    print("No items were ordered.")

print("Thank you for visiting!")