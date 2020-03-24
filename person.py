
class Person(object):
    """ Defines information for a person """
    
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address
    
    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def get_name(self):
        return self.name

    def __str__(self):
        return "Name: " + self.name + \
               "\nAddress: " + self.address + \
               "\nPhone: " + self.phone
