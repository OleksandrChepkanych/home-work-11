from collections import UserDict

class Field:
    def __init__(self, value) -> None:
        self.value = value
   
    def __eq__(self, other):
        return self.value == other.value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record():
    def __init__(self, name, phone=None):
        self.name = name
        if phone:
            self.phones = [phone]
        else:
            self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(phone)

    def dell_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
    
    def edit_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
            self.phones.append(input("Enter neu phone: "))

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record
   


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')