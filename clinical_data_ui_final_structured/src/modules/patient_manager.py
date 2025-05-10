import csv
import uuid

PATIENT_FILE = 'data/Patient_data.csv'

class PatientManager:
    def add_patient(self, patient_data):
        with open(PATIENT_FILE, 'a', newline='') as file:
            fieldnames = ['Patient_ID','Visit_ID','Visit_time','Visit_department','Gender','Race','Age','Ethnicity','Insurance','Zip_code','Chief_complaint']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(patient_data)

    def remove_patient(self, patient_id):
        rows = []
        found = False
        with open(PATIENT_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Patient_ID'] != patient_id:
                    rows.append(row)
                else:
                    found = True
        with open(PATIENT_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        return found

    def retrieve_patient(self, patient_id):
        latest_visit = None
        with open(PATIENT_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Patient_ID'] == patient_id:
                    if (not latest_visit) or row['Visit_time'] > latest_visit['Visit_time']:
                        latest_visit = row
        return latest_visit

    def count_visits(self, date):
        count = 0
        with open(PATIENT_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Visit_time'] == date:
                    count += 1
        return count
