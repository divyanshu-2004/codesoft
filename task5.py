import json

contacts = {}

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            global contacts
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    if name in contacts:
        print("A contact with this name already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        save_contacts()
        print("Contact added successfully.")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("\nNo contacts found.")

def search_contact():
    search_term = input("Enter name or phone number to search: ").strip()
    results = {name: details for name, details in contacts.items() if search_term in name or search_term in details['phone']}
    
    if results:
        print("\nSearch Results:")
        for name, details in results.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No matching contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave the field blank if you do not want to update it.")
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        address = input("Enter new address: ").strip()
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
            
        save_contacts()
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    load_contacts()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
