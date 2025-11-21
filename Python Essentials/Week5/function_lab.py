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
    print("4. Days, hours, and minutes to seconds")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")#Awaits user input

    if choice == "1":
        try:
            days = int(input("Enter number of days: "))
            print(str(days) + " days = " + str(days_to_seconds(days)) + " seconds")#Prints the entered amount of days and the seconds in them
        except:
            print("Not a valid number.")

    elif choice == "2":
        try:
            hours = int(input("Enter number of hours: "))
            print(str(hours) + " hours = " + str(hours_to_seconds(hours)) + " seconds")#Prints hours and the seconds in them
        except:
            print("Not a valid number.")

    elif choice == "3":
        try:
            minutes = int(input("Enter number of minutes: "))
            print(str(minutes) + " minutes = " + str(minutes_to_seconds(minutes)) + " seconds")#Prints minutes and the seconds in them
        except:
            print("Not a valid number.")
    elif choice == "4":
        try:
            days = int(input("Enter number of days: "))
            hours = int(input("Enter number of hours: "))
            minutes = int(input("Enter number of minutes: "))
            
            total_seconds = days_to_seconds(days) + hours_to_seconds(hours) + minutes_to_seconds(minutes) #Adds the totals
            print(str(days) + " days, " + str(hours) + " hours, and " + str(minutes) + " minutes = " + str(total_seconds) + " seconds") #Gives the user all the values they entered converted into seconds added together
        except:
            print("Please enter valid numbers only.")

    elif choice == "5":
        print("Goodbye!")
        break #Breaks the simple loop
    else:
        print("Invalid choice. Please select an option (1-5).")
