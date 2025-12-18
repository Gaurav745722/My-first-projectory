# class Book:
#     def __init__(self, book_id, title, author, quantity):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.quantity = quantity

#     def __str__(self):
#         return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Quantity: {self.quantity}"


# class Member:
#     def __init__(self, member_id, name):
#         self.member_id = member_id
#         self.name = name
#         self.books_borrowed = []

#     def borrow_book(self, book):
#         if len(self.books_borrowed) < 3:  # Limit of 3 books per member
#             self.books_borrowed.append(book)
#             book.quantity -= 1
#             print(f"Book '{book.title}' borrowed by {self.name}.")
#         else:
#             print(f"{self.name} has already borrowed the maximum number of books.")

#     def return_book(self, book):
#         if book in self.books_borrowed:
#             self.books_borrowed.remove(book)
#             book.quantity += 1
#             print(f"Book '{book.title}' returned by {self.name}.")
#         else:
#             print(f"{self.name} did not borrow this book.")

#     def display_borrowed_books(self):
#         if not self.books_borrowed:
#             print(f"{self.name} has no borrowed books.")
#         else:
#             print(f"{self.name}'s borrowed books:")
#             for book in self.books_borrowed:
#                 print(f"- {book.title}")


# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []

#     def add_book(self, book_id, title, author, quantity):
#         if any(book.book_id == book_id for book in self.books):
#             print("Book ID already exists.")
#         else:
#             self.books.append(Book(book_id, title, author, quantity))
#             print("Book added successfully.")

#     def remove_book(self, book_id):
#         book = self.find_book_by_id(book_id)
#         if book:
#             self.books.remove(book)
#             print("Book removed successfully.")
#         else:
#             print("Book not found.")

#     def find_book_by_id(self, book_id):
#         for book in self.books:
#             if book.book_id == book_id:
#                 return book
#         return None

#     def find_book_by_title(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower():
#                 return book
#         return None

#     def add_member(self, member_id, name):
#         if any(member.member_id == member_id for member in self.members):
#             print("Member ID already exists.")
#         else:
#             self.members.append(Member(member_id, name))
#             print("Member added successfully.")

#     def remove_member(self, member_id):
#         member = self.find_member_by_id(member_id)
#         if member:
#             self.members.remove(member)
#             print("Member removed successfully.")
#         else:
#             print("Member not found.")

#     def find_member_by_id(self, member_id):
#         for member in self.members:
#             if member.member_id == member_id:
#                 return member
#         return None

#     def find_member_by_name(self, name):
#         for member in self.members:
#             if member.name.lower() == name.lower():
#                 return member
#         return None

#     def issue_book(self, member_id, book_id):
#         member = self.find_member_by_id(member_id)
#         book = self.find_book_by_id(book_id)
#         if member and book:
#             if book.quantity > 0:
#                 member.borrow_book(book)
#             else:
#                 print("Book is out of stock.")
#         else:
#             print("Member or book not found.")

#     def return_book(self, member_id, book_id):
#         member = self.find_member_by_id(member_id)
#         book = self.find_book_by_id(book_id)
#         if member and book:
#             member.return_book(book)
#         else:
#             print("Member or book not found.")

#     def display_all_books(self):
#         if not self.books:
#             print("No books in the library.")
#         else:
#             print("All books in the library:")
#             for book in self.books:
#                 print(book)

#     def display_all_members(self):
#         if not self.members:
#             print("No members in the library.")
#         else:
#             print("All members in the library:")
#             for member in self.members:
#                 print(f"ID: {member.member_id}, Name: {member.name}")


# def display_menu():
#     print("\nWelcome to the Library Management System")
#     print("1. Add Book")
#     print("2. Remove Book")
#     print("3. Search Book by ID")
#     print("4. Search Book by Title")
#     print("5. Add Member")
#     print("6. Remove Member")
#     print("7. Issue Book to Member")
#     print("8. Return Book from Member")
#     print("9. Display All Books")
#     print("10. Display All Members")
#     print("11. Display Borrowed Books by Member")
#     print("12. Exit")


# def main():
#     library = Library()

#     while True:
#         display_menu()
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             book_id = input("Enter book ID: ")
#             title = input("Enter book title: ")
#             author = input("Enter book author: ")
#             quantity = int(input("Enter book quantity: "))
#             library.add_book(book_id, title, author, quantity)

#         elif choice == "2":
#             book_id = input("Enter book ID to remove: ")
#             library.remove_book(book_id)

#         elif choice == "3":
#             book_id = input("Enter book ID to search: ")
#             book = library.find_book_by_id(book_id)
#             if book:
#                 print(book)
#             else:
#                 print("Book not found.")

#         elif choice == "4":
#             title = input("Enter book title to search: ")
#             book = library.find_book_by_title(title)
#             if book:
#                 print(book)
#             else:
#                 print("Book not found.")

#         elif choice == "5":
#             member_id = input("Enter member ID: ")
#             name = input("Enter member name: ")
#             library.add_member(member_id, name)

#         elif choice == "6":
#             member_id = input("Enter member ID to remove: ")
#             library.remove_member(member_id)

#         elif choice == "7":
#             member_id = input("Enter member ID: ")
#             book_id = input("Enter book ID to issue: ")
#             library.issue_book(member_id, book_id)

#         elif choice == "8":
#             member_id = input("Enter member ID: ")
#             book_id = input("Enter book ID to return: ")
#             library.return_book(member_id, book_id)

#         elif choice == "9":
#             library.display_all_books()

#         elif choice == "10":
#             library.display_all_members()

#         elif choice == "11":
#             member_id = input("Enter member ID to display borrowed books: ")
#             member = library.find_member_by_id(member_id)
#             if member:
#                 member.display_borrowed_books()
#             else:
#                 print("Member not found.")

#         elif choice == "12":
#             print("Thank you for using the Library Management System. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()







# import json
# import os

# # File paths for data storage
# PERSONNEL_FILE = "personnel.json"
# EQUIPMENT_FILE = "equipment.json"
# MISSION_FILE = "mission.json"
# OPERATION_FILE = "operation.json"


# class Personnel:
#     def __init__(self, id, name, rank, role):
#         self.id = id
#         self.name = name
#         self.rank = rank
#         self.role = role

#     def __str__(self):
#         return f"ID: {self.id}, Name: {self.name}, Rank: {self.rank}, Role: {self.role}"


# class Equipment:
#     def __init__(self, id, name, type, status="Available"):
#         self.id = id
#         self.name = name
#         self.type = type
#         self.status = status

#     def __str__(self):
#         return f"ID: {self.id}, Name: {self.name}, Type: {self.type}, Status: {self.status}"


# class Mission:
#     def __init__(self, id, name, description, personnel_assigned=None, equipment_assigned=None):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.personnel_assigned = personnel_assigned if personnel_assigned else []
#         self.equipment_assigned = equipment_assigned if equipment_assigned else []

#     def __str__(self):
#         return (f"ID: {self.id}, Name: {self.name}, Description: {self.description}, "
#                 f"Personnel Assigned: {len(self.personnel_assigned)}, Equipment Assigned: {len(self.equipment_assigned)}")


# class Operation:
#     def __init__(self, id, name, description, missions=None):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.missions = missions if missions else []

#     def __str__(self):
#         return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Missions: {len(self.missions)}"


# class DefenseManagement:
#     def __init__(self):
#         self.personnel = []
#         self.equipment = []
#         self.missions = []
#         self.operations = []
#         self.load_data()

#     def add_personnel(self, personnel):
#         self.personnel.append(personnel)
#         self.save_data()

#     def remove_personnel(self, personnel_id):
#         self.personnel = [p for p in self.personnel if p.id != personnel_id]
#         self.save_data()

#     def add_equipment(self, equipment):
#         self.equipment.append(equipment)
#         self.save_data()

#     def remove_equipment(self, equipment_id):
#         self.equipment = [e for e in self.equipment if e.id != equipment_id]
#         self.save_data()

#     def add_mission(self, mission):
#         self.missions.append(mission)
#         self.save_data()

#     def remove_mission(self, mission_id):
#         self.missions = [m for m in self.missions if m.id != mission_id]
#         self.save_data()

#     def add_operation(self, operation):
#         self.operations.append(operation)
#         self.save_data()

#     def remove_operation(self, operation_id):
#         self.operations = [o for o in self.operations if o.id != operation_id]
#         self.save_data()

#     def find_personnel_by_id(self, personnel_id):
#         for p in self.personnel:
#             if p.id == personnel_id:
#                 return p
#         return None

#     def find_equipment_by_id(self, equipment_id):
#         for e in self.equipment:
#             if e.id == equipment_id:
#                 return e
#         return None

#     def find_mission_by_id(self, mission_id):
#         for m in self.missions:
#             if m.id == mission_id:
#                 return m
#         return None

#     def find_operation_by_id(self, operation_id):
#         for o in self.operations:
#             if o.id == operation_id:
#                 return o
#         return None

#     def assign_personnel_to_mission(self, personnel_id, mission_id):
#         personnel = self.find_personnel_by_id(personnel_id)
#         mission = self.find_mission_by_id(mission_id)
#         if personnel and mission:
#             mission.personnel_assigned.append(personnel)
#             self.save_data()
#             print(f"Personnel {personnel.name} assigned to mission {mission.name}.")
#         else:
#             print("Personnel or mission not found.")

#     def assign_equipment_to_mission(self, equipment_id, mission_id):
#         equipment = self.find_equipment_by_id(equipment_id)
#         mission = self.find_mission_by_id(mission_id)
#         if equipment and mission:
#             mission.equipment_assigned.append(equipment)
#             equipment.status = "Assigned"
#             self.save_data()
#             print(f"Equipment {equipment.name} assigned to mission {mission.name}.")
#         else:
#             print("Equipment or mission not found.")

#     def save_data(self):
#         data = {
#             "personnel": [vars(p) for p in self.personnel],
#             "equipment": [vars(e) for e in self.equipment],
#             "missions": [vars(m) for m in self.missions],
#             "operations": [vars(o) for o in self.operations],
#         }
#         with open(PERSONNEL_FILE, "w") as f:
#             json.dump(data["personnel"], f)
#         with open(EQUIPMENT_FILE, "w") as f:
#             json.dump(data["equipment"], f)
#         with open(MISSION_FILE, "w") as f:
#             json.dump(data["missions"], f)
#         with open(OPERATION_FILE, "w") as f:
#             json.dump(data["operations"], f)

#     def load_data(self):
#         if os.path.exists(PERSONNEL_FILE):
#             with open(PERSONNEL_FILE, "r") as f:
#                 self.personnel = [Personnel(**p) for p in json.load(f)]
#         if os.path.exists(EQUIPMENT_FILE):
#             with open(EQUIPMENT_FILE, "r") as f:
#                 self.equipment = [Equipment(**e) for e in json.load(f)]
#         if os.path.exists(MISSION_FILE):
#             with open(MISSION_FILE, "r") as f:
#                 self.missions = [Mission(**m) for m in json.load(f)]
#         if os.path.exists(OPERATION_FILE):
#             with open(OPERATION_FILE, "r") as f:
#                 self.operations = [Operation(**o) for o in json.load(f)]


# def display_menu():
#     print("\nDefense Management System")
#     print("1. Add Personnel")
#     print("2. Remove Personnel")
#     print("3. Add Equipment")
#     print("4. Remove Equipment")
#     print("5. Add Mission")
#     print("6. Remove Mission")
#     print("7. Add Operation")
#     print("8. Remove Operation")
#     print("9. Assign Personnel to Mission")
#     print("10. Assign Equipment to Mission")
#     print("11. Display All Personnel")
#     print("12. Display All Equipment")
#     print("13. Display All Missions")
#     print("14. Display All Operations")
#     print("15. Exit")


# def main():
#     defense_system = DefenseManagement()

#     while True:
#         display_menu()
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             id = input("Enter personnel ID: ")
#             name = input("Enter personnel name: ")
#             rank = input("Enter personnel rank: ")
#             role = input("Enter personnel role: ")
#             defense_system.add_personnel(Personnel(id, name, rank, role))

#         elif choice == "2":
#             id = input("Enter personnel ID to remove: ")
#             defense_system.remove_personnel(id)

#         elif choice == "3":
#             id = input("Enter equipment ID: ")
#             name = input("Enter equipment name: ")
#             type = input("Enter equipment type: ")
#             defense_system.add_equipment(Equipment(id, name, type))

#         elif choice == "4":
#             id = input("Enter equipment ID to remove: ")
#             defense_system.remove_equipment(id)

#         elif choice == "5":
#             id = input("Enter mission ID: ")
#             name = input("Enter mission name: ")
#             description = input("Enter mission description: ")
#             defense_system.add_mission(Mission(id, name, description))

#         elif choice == "6":
#             id = input("Enter mission ID to remove: ")
#             defense_system.remove_mission(id)

#         elif choice == "7":
#             id = input("Enter operation ID: ")
#             name = input("Enter operation name: ")
#             description = input("Enter operation description: ")
#             defense_system.add_operation(Operation(id, name, description))

#         elif choice == "8":
#             id = input("Enter operation ID to remove: ")
#             defense_system.remove_operation(id)

#         elif choice == "9":
#             personnel_id = input("Enter personnel ID: ")
#             mission_id = input("Enter mission ID: ")
#             defense_system.assign_personnel_to_mission(personnel_id, mission_id)

#         elif choice == "10":
#             equipment_id = input("Enter equipment ID: ")
#             mission_id = input("Enter mission ID: ")
#             defense_system.assign_equipment_to_mission(equipment_id, mission_id)

#         elif choice == "11":
#             for p in defense_system.personnel:
#                 print(p)

#         elif choice == "12":
#             for e in defense_system.equipment:
#                 print(e)

#         elif choice == "13":
#             for m in defense_system.missions:
#                 print(m)

#         elif choice == "14":
#             for o in defense_system.operations:
#                 print(o)

#         elif choice == "15":
#             print("Exiting the Defense Management System. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()





import hashlib
import random
import time

# ---- Personnel Management ----
class Personnel:
    def __init__(self, id, name, rank, unit, skills):
        self.id = id
        self.name = name
        self.rank = rank
        self.unit = unit
        self.skills = skills  # List of skills

    def __str__(self):
        return f'{self.rank} {self.name} ({self.unit})'

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)

    def update_rank(self, new_rank):
        self.rank = new_rank

class Officer(Personnel):
    def __init__(self, id, name, rank, unit, skills, command_units):
        super().__init__(id, name, rank, unit, skills)
        self.command_units = command_units  # Units the officer is responsible for

    def __str__(self):
        return f'Officer {self.name}, Rank: {self.rank}, Commanding: {", ".join(self.command_units)}'

class Soldier(Personnel):
    def __init__(self, id, name, rank, unit, skills, equipment_assigned):
        super().__init__(id, name, rank, unit, skills)
        self.equipment_assigned = equipment_assigned  # List of assigned equipment

    def __str__(self):
        return f'Soldier {self.name}, Rank: {self.rank}, Assigned Equipment: {", ".join(self.equipment_assigned)}'

    def assign_equipment(self, equipment):
        if equipment not in self.equipment_assigned:
            self.equipment_assigned.append(equipment)

    def remove_equipment(self, equipment):
        if equipment in self.equipment_assigned:
            self.equipment_assigned.remove(equipment)

# ---- Equipment Management ----
class Equipment:
    def __init__(self, id, name, type, status):
        self.id = id
        self.name = name
        self.type = type
        self.status = status

    def __str__(self):
        return f'{self.type}: {self.name} - Status: {self.status}'

# ---- Inventory Management ----
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
        else:
            print(f"Not enough {item} in inventory.")

    def show_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

# ---- Mission Management ----
class Mission:
    def __init__(self, mission_id, description, personnel_needed, equipment_needed):
        self.mission_id = mission_id
        self.description = description
        self.personnel_needed = personnel_needed
        self.equipment_needed = equipment_needed

    def assign_personnel(self, personnel_list):
        self.assigned_personnel = [p for p in personnel_list if p.rank in self.personnel_needed]

    def assign_equipment(self, inventory):
        self.assigned_equipment = []
        for equipment in self.equipment_needed:
            if equipment in inventory.items and inventory.items[equipment] > 0:
                self.assigned_equipment.append(equipment)
                inventory.remove_item(equipment, 1)

    def mission_details(self):
        print(f"Mission ID: {self.mission_id}")
        print(f"Description: {self.description}")
        print(f"Personnel: {[str(p) for p in self.assigned_personnel]}")
        print(f"Equipment: {self.assigned_equipment}")

# ---- Communication System ----
class CommunicationSystem:
    def __init__(self):
        self.messages = []  # Store all messages for audit
        self.encryption_key = self.generate_encryption_key()

    def generate_encryption_key(self):
        """Generates a simple encryption key"""
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()

    def encrypt_message(self, message):
        """Encrypt the message with a simple algorithm"""
        return ''.join(chr(ord(c) + len(self.encryption_key) % 256) for c in message)

    def decrypt_message(self, encrypted_message):
        """Decrypt the message"""
        return ''.join(chr(ord(c) - len(self.encryption_key) % 256) for c in encrypted_message)

    def send_message(self, sender, recipient, message):
        encrypted_message = self.encrypt_message(message)
        timestamp = time.time()
        self.messages.append({
            'sender': sender,
            'recipient': recipient,
            'message': encrypted_message,
            'timestamp': timestamp
        })
        print(f"Message sent from {sender} to {recipient}: {encrypted_message}")
        return encrypted_message

    def retrieve_message(self, sender, recipient):
        for msg in self.messages:
            if msg['sender'] == sender and msg['recipient'] == recipient:
                return self.decrypt_message(msg['message'])
        return None

# ---- Main Defense Management System ----
class DefenseManagementSystem:
    def __init__(self):
        self.personnel_list = []
        self.equipment_list = []
        self.inventory = Inventory()
        self.missions = []
        self.communication = CommunicationSystem()

    def add_personnel(self, personnel):
        self.personnel_list.append(personnel)

    def add_equipment(self, equipment):
        self.equipment_list.append(equipment)

    def create_mission(self, mission):
        self.missions.append(mission)

    def show_all_personnel(self):
        for p in self.personnel_list:
            print(p)

    def show_all_equipment(self):
        for eq in self.equipment_list:
            print(eq)

    def show_inventory(self):
        self.inventory.show_inventory()

    def run_mission(self, mission_id):
        mission = next((m for m in self.missions if m.mission_id == mission_id), None)
        if mission:
            mission.assign_personnel(self.personnel_list)
            mission.assign_equipment(self.inventory)
            mission.mission_details()
        else:
            print(f"Mission ID {mission_id} not found.")

# Example Usage
if __name__ == "__main__":
    defense_system = DefenseManagementSystem()

    # Add Personnel
    soldier1 = Soldier(1, "John Doe", "Private", "Infantry", ["Sniper"], ["M16"])
    soldier2 = Soldier(2, "Jane Smith", "Sergeant", "Artillery", ["Medic"], ["First Aid Kit"])

    defense_system.add_personnel(soldier1)
    defense_system.add_personnel(soldier2)

    # Add Equipment
    rifle = Equipment(1, "M16", "Rifle", "Available")
    tank = Equipment(2, "Abrams", "Tank", "Deployed")

    defense_system.add_equipment(rifle)
    defense_system.add_equipment(tank)

    # Add Items to Inventory
    defense_system.inventory.add_item("Ammunition", 500)
    defense_system.inventory.add_item("Medical Supplies", 100)

    # Create Mission
    mission = Mission(1, "Defend the border", ["Private", "Sergeant"], ["Rifle", "Tank"])
    defense_system.create_mission(mission)

    # Run Mission
    defense_system.run_mission(1)

    # Show All Personnel, Equipment, and Inventory
    print("\nPersonnel List:")
    defense_system.show_all_personnel()
    
    print("\nEquipment List:")
    defense_system.show_all_equipment()
    
    print("\nInventory:")
    defense_system.show_inventory()

    # Communication
    defense_system.communication.send_message("Sergeant Jane", "Private John", "Prepare for mission!")
    print("\nReceived Message:", defense_system.communication.retrieve_message("Sergeant Jane", "Private John"))
