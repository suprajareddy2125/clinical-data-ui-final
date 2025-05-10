class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class AdminUser(User):
    def __init__(self, username):
        super().__init__(username, 'admin')

class ManagementUser(User):
    def __init__(self, username):
        super().__init__(username, 'management')

class ClinicianUser(User):
    def __init__(self, username):
        super().__init__(username, 'clinician')

class NurseUser(User):
    def __init__(self, username):
        super().__init__(username, 'nurse')
