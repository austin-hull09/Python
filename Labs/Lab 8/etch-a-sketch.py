# -----------------------------------------------------
# CSCI 127, Lab 8
# October 24, 2017
# Austin Hull
# -----------------------------------------------------

class Contact:
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone

    def get_cell_number(self):
        return self.phone

    def get_area_code(self):
        return self.phone[:3]

    def set_first_name(self, first):
        self.first = first

    def set_title(self, title):
        self.first = title + " " + self.first
    
    def __str__(self):
        return (self.first + " " + self.last).ljust(27) + self.phone

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        print(person)
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
