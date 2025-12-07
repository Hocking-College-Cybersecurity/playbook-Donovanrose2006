import csv
filename = "./mydata.csv"
def save_data(filename, data):
    fieldnames = ["name", "age", "eyes"]

    with open(filename, "w", newline="") as file:
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader()
        write.writerows(data)
def read_data(filename):

    read_in_data = []
    with open(filename, "r", newline="") as file:
        read = csv.DictReader(file)
        for row in read:
            read_in_data.append(row)
    return read_in_data

dummy = [{"name":'A',"age":"3","eyes":"True"},
        {"name":'B',"age":"3542","eyes":"False"}]
save_data(filename , dummy)
print(read_data(filename))