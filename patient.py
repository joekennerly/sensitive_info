class Patient:

    def __init__(self, social, dob, acc_num, first, last, address):
        self.social_security = social
        self.date_of_birth = dob
        self.account_number = acc_num
        self.first_name = first
        self.last_name = last
        self.address = address

    def __str__(self):
        return f'{self.social_security} {self.date_of_birth} {self.account_number} {self.first_name} {self.last_name} {self.address}'

mr_mike = Patient(45, "08/31/45", 3000, "mike", "pence", "123 Street St")
print(mr_mike)