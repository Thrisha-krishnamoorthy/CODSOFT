def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully.")
def view_contacts(contacts):
    if contacts:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("No contacts found.")
def search_contact(contacts):
    search_term = input("Enter Name or Phone Number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term in name or search_term in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found.")
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new Phone Number: ")
        email = input("Enter new Email: ")
        address = input("Enter new Address: ")
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} updated ")
    else:
        print("Contact not found.")
def delete_contact(contacts):
    name = input("Enter the name of  contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted ")
    else:
        print("Contact not found.")
def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice : ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting ")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
