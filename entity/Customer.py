class Customer:
    def __init__(self, ccode, cus_name, phone):
        self._ccode = ccode
        self._cus_name = cus_name
        self._phone = phone

    @property
    def ccode(self):
        return self._ccode

    @ccode.setter
    def ccode(self, value):
        self._ccode = value

    @property
    def cus_name(self):
        return self._cus_name

    @cus_name.setter
    def cus_name(self, value):
        self._cus_name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def __str__(self):
        return f"Customer: {self._ccode}, Name: {self._cus_name}, Phone: {self._phone}"

# Example usage:
# customer1 = Customer("CC001", "John Doe", "1234567890")
# print(customer1.cus_name)  # Output: John Doe

# customer1.cus_name = "Jane Smith"
# print(customer1)  # Output: Customer: CC001, Name: Jane Smith, Phone: 1234567890
