
# Clinical Data Warehouse UI Application

This project is a Tkinter-based graphical user interface (GUI) for interacting with a clinical data warehouse system. It is built for HI 741 Spring 2025 Final Project and supports various user roles (admin, management, clinician, nurse) to securely access and manage patient data.

## Features

- **Login System** with credential validation from `Credentials.csv`
- **Role-Based Menus**: 
  - `admin`: Count Visits
  - `management`: Generate Key Statistics
  - `clinician/nurse`: Add, Remove, Retrieve Patient, Count Visits, View Note
- **Patient Management**: Add, remove, and retrieve patient info from `Patient_data.csv`
- **Clinical Notes**: View patient notes stored in `Notes.csv`
- **Statistics**: Generate visualizations and statistics of patient visits
- **Usage Logs**: Track login and user actions (can be added to enhance auditability)

## Directory Structure

```
project_root/
├── main.py
├── modules/
│   ├── auth.py
│   ├── user.py
│   ├── patient_manager.py
│   ├── notes_manager.py
│   └── statistics_manager.py
├── Patient_data.csv
├── Credentials.csv
├── Notes.csv
└── statistics.png
```

## Setup Instructions

### Environment

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Run the Program

```bash
python main.py
```

## Required CSV Files

- `Credentials.csv`: Contains Username, Password, and Role
- `Patient_data.csv`: Patient information
- `Notes.csv`: Clinical notes associated with patient visits

## Requirements File

```
tk
pandas
matplotlib
```

## Notes

- This program adheres to object-oriented principles.
- Classes are organized by functionality for maintainability and scalability.
- A UML diagram is provided (`UML.png`) as part of the design documentation.

---

Supraja reddy Bathula, HI 741 — Clinical Data Warehouse Project
