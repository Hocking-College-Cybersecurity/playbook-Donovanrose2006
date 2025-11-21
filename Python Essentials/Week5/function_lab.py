def days_to_seconds(days): #Converts days into seconds
    return days * 24 * 60 * 60 

def hours_to_seconds(hours): #Converts hours into seconds
    return hours * 60 * 60

def minutes_to_seconds(minutes): #Converts minutes into seconds
    return minutes * 60

while(True): #Creates a simple loop
    print("1. Days to seconds")
    print("2. Hours to seconds")
    print("3. Minutes to seconds")
    print("4. Exit")
    choice = input("Choose an option (1, 2, 3, or 4): ")#Awaits user input

    if choice == "1":
        value = input("Enter number of days: ")#Waits for days to convert to seconds
        try:
            days = int(value)
            print(str(days) + " days = " + str(days_to_seconds(days)) + " seconds")#Prints the entered amount of days and the seconds in them
        except:
            print("Not a valid number.")

    elif choice == "2":
        value = input("Enter number of hours: ")#Same thing with hours
        try:
            hours = int(value)
            print(str(hours) + " hours = " + str(hours_to_seconds(hours)) + " seconds")#Prints hours and the seconds in them
        except:
            print("Not a valid number.")

    elif choice == "3":
        value = input("Enter number of minutes: ")#Same with minutes
        try:
            minutes = int(value)
            print(str(minutes) + " minutes = " + str(minutes_to_seconds(minutes)) + " seconds")#Prints minutes and the seconds in them
        except:
            print("Not a valid number.")
    elif choice == "4":
        print("Goodbye!")
        break #Breaks the simple loop
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
