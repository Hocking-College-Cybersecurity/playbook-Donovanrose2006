def add_patient(patients): #Fuction for adding patients

    patient_id = input("Enter patient ID: ")
    if patient_id == "":
        print("Error: Patient ID cannot be blank.")
        return

    if patient_id in patients:
        print("Error: That ID already exists.")
        return
    
    name = input("Enter patient name: ")
    if name == "":
        print("Error: Name cannot be blank.")
        return

    age = input("Enter patient age: ")
    if age == "":
        print("Error: Age cannot be blank.")
        return

    try:
        age = int(age)
    except:
        print("Error: Age must be a number.")
        return
    
    patients[patient_id] = {"name": name, "age": age}
    print("Patient added successfully.")

def view_patient(patients): #Function for viewing patients using IDs
    patient_id = input("Enter patient ID: ")

    if patient_id == "":
        print("Error: Patient ID cannot be blank.")
        return

    if patient_id not in patients:
        print("Error: No patient with that ID.")
        return
    
    patient = patients[patient_id]
    print("Name: " + patient["name"])
    print("Age: " + str(patient["age"]))

def list_patients(patients): # Funtion for viewing all patient names and ages
    if len(patients) == 0:
        print("No patients recorded yet.")
        return
    
    for pid in patients:
        print(pid + ": " + patients[pid]["name"])

patients = {} #Where the dictionary of patients will go

while True:
    print("\n1. Add patient")
    print("2. View patient")
    print("3. List all patients")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "":
        print("Error: Choice cannot be blank.")
        continue

    if choice == "1":
        add_patient(patients)
    elif choice == "2":
        view_patient(patients)
    elif choice == "3":
        list_patients(patients)
    elif choice == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid choice.")
#All of this is subject to change, just a prototype. Haven't decided if I will rework everything yet either.