"""Python Final Project - Small Clinic Patient Recorder"""
"""Simple Program with adding patients, discharging patients, viewing specific patients, and listing all current patients."""
"""Make sure the program is ran in the same directory as the .py file."""
"""Basic ASCII is also included to make menus easier to navigate."""

import csv  # Importing for saving and loading

DATA_FILE = "./patients_data.csv" 


def get_next_patient_id(patients):
    """Return next patient ID. Will never repeat."""
    max_id = 0
    for pid in patients:
        try:
            num = int(pid)
            if num > max_id:
                max_id = num
        except:
            pass
    return str(max_id + 1)


def add_patient(patients):
    """Add a new patient."""
    print("\nAdd Patient")

    patient_id = get_next_patient_id(patients)
    print("Assigned patient ID: " + patient_id)

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
        if age <= 0:
            print("Error: Age must be greater than 0.")
            return
    except:
        print("Error: Age must be a number.")
        return

    condition = input("Enter condition: ")
    if condition == "":
        print("Error: Condition cannot be blank.")
        return

    patients[patient_id] = {
        "name": name,
        "age": age,
        "conditions": [condition],
        "discharged": False #A new record will never be automatically discharged.
    }

    print("Patient added.")


def view_patient(patients):
    """View patient by ID."""
    print("\nView Patient")

    patient_id = input("Enter patient ID: ")
    if patient_id == "":
        print("Error: Patient ID cannot be blank.")
        return
    if patient_id not in patients:
        print("Error: No patient with that ID.")
        return

    p = patients[patient_id]
    cond_text = ", ".join(p["conditions"]) #More easily readable for users

    print("---------------")
    print("Patient ID: " + patient_id)
    print("Name: " + p["name"])
    print("Age: " + str(p["age"]))
    print("Condition(s): " + cond_text)

    if p["discharged"] == True:
        print("Status: Discharged")

    print("---------------")


def list_patients(patients):
    """List all patients."""
    print("\nList Patients")

    if len(patients) == 0:
        print("No patients recorded.")
        return

    for pid in patients:
        p = patients[pid]
        status = " (Discharged)" if p["discharged"] else ""
        line = "ID: " + pid + " | Name: " + p["name"] + " | Age: " + str(p["age"]) + status
        print(line)


def discharge_patient(patients):
    """Discharge (mark) a patient."""
    print("\nDischarge Patient")

    patient_id = input("Enter patient ID: ")
    if patient_id == "":
        print("Error: Patient ID cannot be blank.")
        return

    if patient_id not in patients:
        print("Error: No patient with that ID.")
        return

    p = patients[patient_id]

    if p["discharged"] == True:
        print("Patient is already discharged.")
        return

    confirm = input("Mark this patient as discharged? Enter y to confirm: ")
    if confirm.lower() == "y":
        p["discharged"] = True
        print("Patient discharged.")
    else: 
        print("Discharge cancelled.")


def save_patients(patients, filename):
    """Save patient records."""
    try:
        fieldnames = ["id", "name", "age", "conditions", "discharged"] # Column names for the CSV file
        
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader() # Writes column names to the first row

            for pid in patients:
                p = patients[pid]

                writer.writerow({
                    "id": pid,
                    "name": p["name"],
                    "age": str(p["age"]),
                    "conditions": ",".join(p["conditions"]),
                    "discharged": "True" if p["discharged"] else "False"
                }) # Write one patient as a row in the CSV file

    except:
        print("Error saving data.")


def load_patients(patients, filename):
    """Load patient records."""
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            patients.clear()

            for row in reader: # Convert string values from the file back into Python readable types
                pid = row["id"]
                name = row["name"]
                age = int(row["age"])
                conditions = row["conditions"].split(",") if row["conditions"] else []
                discharged = (row["discharged"] == "True")

                patients[pid] = {
                    "name": name,
                    "age": age,
                    "conditions": conditions,
                    "discharged": discharged
                }

        print("Patient data loaded from file.")

    except FileNotFoundError: # Easy notification to tell the user that this is their first time using the program/they used it in the wrong directory
        print("No existing data file found. Starting fresh.")


def show_menu():
    """Show the main menu."""
    print("\nPatient Menu")
    print("1. Add patient")
    print("2. View patient")
    print("3. List patients")
    print("4. Discharge patient")
    print("5. Exit")


# Main menu
patients = {}

load_patients(patients, DATA_FILE)

while True:
    show_menu()
    choice = input("Choose (1-5): ")

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
        discharge_patient(patients)
    elif choice == "5":
        save_patients(patients, DATA_FILE)
        print("Exiting Program...")
        break
    else:
        print("Invalid choice.")

    if choice in ["1", "2", "3", "4"]:
        save_patients(patients, DATA_FILE)