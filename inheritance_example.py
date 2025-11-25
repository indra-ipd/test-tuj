class Phone:
    # Class constructor
    def __init__(self, name, color, storage):
        self.name = name
        self.color = color
        self.storage = storage

    def details(self):
        print("This is a", self.color, self.name,
              "with", self.storage, "GB storage")

class Laptop(Phone):
    def get_info(self):
        print("This is a laptop class derived from phone")
        print("Specs: \n Laptop:", self.name,
              "\n Color", self.color,
              "\n Hard disk", self.storage,"TB" )

print("--------------------------------------------")
print("Example of Laptop Instance - inheritance")
# instance for laptop
laptop1 = Laptop("macbook 15", "silver", "2")
laptop1.details()
laptop1.get_info()

print("--------------------------------------------")
print("Example of Phone Instance")
# instance for phone
phone1 = Phone("iPhone14", "Blue", 64)
phone1.details()

print("--------------------------------------------")

laptop2 = Laptop("Chrome book pro", "black", "1")
laptop2.details()
