items = []

choice = ""

while choice != "4":
    print("Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display all items")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item to add: ")
        if item != "":
            items.append(item)
            print("Item added to list.")
        else:
            print("You must enter something to add.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in items:
            items.remove(item) #Found online when researching this. Makes it a lot easier and more intuitive in my opinion.
            print("Item removed from list.")
        else:
            print("Item not found in list.")

    elif choice == "3":
        if len(items) == 0:
            print("The list is empty.")
        else:
            print("Current items:")
            print(items)
    elif choice == "4":
        print("Your final list is" + {items})
        print("Exiting program.")

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
