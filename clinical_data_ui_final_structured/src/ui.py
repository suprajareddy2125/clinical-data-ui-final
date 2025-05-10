import tkinter as tk
from tkinter import messagebox, simpledialog
from modules.auth import authenticate_user
from modules.patient_manager import PatientManager
from modules.notes_manager import NotesManager
from modules.statistics_manager import StatisticsManager
from modules.user import AdminUser, ManagementUser, ClinicianUser, NurseUser
import uuid
import csv
from datetime import datetime

class UIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Clinical Data Warehouse")
        self.patient_manager = PatientManager()
        self.notes_manager = NotesManager()
        self.stats_manager = StatisticsManager()
        self.user = None
        self.usage_log_file = 'data/usage_log.csv'
        self.login_screen()

    def log_usage(self, action, success=True):
        with open(self.usage_log_file, 'a', newline='') as file:
            writer = csv.writer(file)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([
                self.user.username if self.user else 'UNKNOWN',
                self.user.role if self.user else 'UNKNOWN',
                now,
                action,
                'Success' if success else 'Failure'
            ])

    def login_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text="Username:").grid(row=0, column=0)
        tk.Label(self.master, text="Password:").grid(row=1, column=0)
        username_entry = tk.Entry(self.master)
        password_entry = tk.Entry(self.master, show='*')
        username_entry.grid(row=0, column=1)
        password_entry.grid(row=1, column=1)

        def attempt_login():
            username = username_entry.get()
            password = password_entry.get()
            role = authenticate_user(username, password)
            if role:
                if role == 'admin':
                    self.user = AdminUser(username)
                elif role == 'management':
                    self.user = ManagementUser(username)
                elif role == 'clinician':
                    self.user = ClinicianUser(username)
                elif role == 'nurse':
                    self.user = NurseUser(username)
                self.log_usage("Login")
                self.menu_screen()
            else:
                self.user = None
                self.log_usage("Failed Login", success=False)
                messagebox.showerror("Login Failed", "Invalid credentials.")

        tk.Button(self.master, text="Login", command=attempt_login).grid(row=2, column=1)

    def menu_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text=f"Welcome {self.user.username} ({self.user.role})").pack()
        if self.user.role == 'admin':
            tk.Button(self.master, text="Count Visits", command=self.count_visits).pack()
        elif self.user.role == 'management':
            tk.Button(self.master, text="Generate Key Statistics", command=self.generate_statistics).pack()
        elif self.user.role in ['clinician', 'nurse']:
            tk.Button(self.master, text="Add Patient", command=self.add_patient).pack()
            tk.Button(self.master, text="Remove Patient", command=self.remove_patient).pack()
            tk.Button(self.master, text="Retrieve Patient", command=self.retrieve_patient).pack()
            tk.Button(self.master, text="Count Visits", command=self.count_visits).pack()
            tk.Button(self.master, text="View Note", command=self.view_note).pack()
        tk.Button(self.master, text="Exit", command=self.master.quit).pack()

    def add_patient(self):
        patient_data = {}
        fields = ['Patient_ID','Visit_time','Visit_department','Gender','Race','Age','Ethnicity','Insurance','Zip_code','Chief_complaint']
        patient_data['Patient_ID'] = simpledialog.askstring("Add Patient", "Enter Patient ID:")
        patient_data['Visit_ID'] = str(uuid.uuid4())
        for field in fields[1:]:
            patient_data[field] = simpledialog.askstring("Add Patient", f"Enter {field}:")
        self.patient_manager.add_patient(patient_data)
        self.log_usage("Add Patient")
        messagebox.showinfo("Success", "Patient added.")

    def remove_patient(self):
        pid = simpledialog.askstring("Remove Patient", "Enter Patient ID to remove:")
        if self.patient_manager.remove_patient(pid):
            self.log_usage("Remove Patient")
            messagebox.showinfo("Removed", "Patient removed.")
        else:
            self.log_usage("Remove Patient - Not Found", success=False)
            messagebox.showwarning("Not Found", "Patient ID not found.")

    def retrieve_patient(self):
        pid = simpledialog.askstring("Retrieve Patient", "Enter Patient ID:")
        patient = self.patient_manager.retrieve_patient(pid)
        if patient:
            self.log_usage("Retrieve Patient")
            info = "\n".join([f"{k}: {v}" for k, v in patient.items()])
            messagebox.showinfo("Patient Info", info)
        else:
            self.log_usage("Retrieve Patient - Not Found", success=False)
            messagebox.showwarning("Not Found", "Patient ID not found.")

    def count_visits(self):
        date = simpledialog.askstring("Count Visits", "Enter date (YYYY-MM-DD):")
        count = self.patient_manager.count_visits(date)
        self.log_usage("Count Visits")
        messagebox.showinfo("Visit Count", f"Total visits on {date}: {count}")

    def view_note(self):
        pid = simpledialog.askstring("View Note", "Enter Patient ID:")
        date = simpledialog.askstring("View Note", "Enter Visit Date (YYYY-MM-DD):")
        notes = self.notes_manager.view_note(pid, date)
        if notes:
            self.log_usage("View Note")
            for note in notes:
                messagebox.showinfo(f"Note {note['Note_ID']}", note['Note_text'])
        else:
            self.log_usage("View Note - Not Found", success=False)
            messagebox.showwarning("Not Found", "No notes found for that patient and date.")

    def generate_statistics(self):
        file = self.stats_manager.generate_key_statistics()
        self.log_usage("Generate Statistics")
        messagebox.showinfo("Statistics Generated", f"Statistics saved to {file}")