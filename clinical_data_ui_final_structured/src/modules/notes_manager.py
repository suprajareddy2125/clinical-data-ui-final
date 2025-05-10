import csv

NOTES_FILE = 'data/Notes.csv'

class NotesManager:
    def view_note(self, patient_id, date):
        notes = []
        with open(NOTES_FILE, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Patient_ID'] == patient_id and row['Visit_time'] == date:
                    notes.append(row)
        return notes
