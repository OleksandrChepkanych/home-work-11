import datetime
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

class Birthday(Field):
    pass

class Record():
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        if phone:
            self.phones = [phone]
        else:
            self.phones = []
        if birthday:
            self.birthday = birthday
        else:
            self.birthday = ''
   
    def add_phone(self, phone):
        self.phones.append(phone)

    def dell_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
    
    def edit_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
            self.phones.append(input("Enter neu phone: "))
    
    def days_to_birthday(self):
        birthday_ = self.birthday.split('.')
        birthday_date = datetime.date(int(birthday_[2]), int(birthday_[1], int(birthday_[0])))
        now = datetime.datetime.today().date()
        day = birthday_date - now
        return abs(day)

    def __str__(self) -> str:
        return f"{str(self)}"

class AddressBook(UserDict):
    current_value = 0
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def __next__(self):
        if self.current_value < len(self.data):
            self.current_value += 1
            return self.current_value
        raise StopIteration


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    birthday = Birthday('27.05.1985')
    rec = Record(name, phone, birthday)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print(ab)
    print(rec.days_to_birthday)