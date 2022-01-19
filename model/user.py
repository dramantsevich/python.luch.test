class User:
    name: str
    surname: str
    phone: str
    email: str
    city: str

    def __init__(self, name: str, surname: str, phone: str, email: str, city: str):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.city = city

    def get_name(self): return self.name
    def set_name(self, name: str): self.name = name

    def get_surname(self): return self.surname
    def set_surname(self, surname: str): self.surname = surname

    def get_phone(self): return self.phone
    def set_phone(self, phone: str): self.phone = phone

    def get_email(self): return self.email
    def set_email(self, email: str): self.email = email

    def get_city(self): return self.city
    def set_city(self, city: str): self.city = city