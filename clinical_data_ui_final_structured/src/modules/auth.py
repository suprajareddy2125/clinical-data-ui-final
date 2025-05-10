import csv

def authenticate_user(username, password):
    with open('data/Credentials.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username and row['Password'] == password:
                return row['Role']
    return None
