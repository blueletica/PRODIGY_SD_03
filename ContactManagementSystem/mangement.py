import json

# Function to load contacts from a file
def load_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        contacts = []
    return contacts

# Function to save contacts to a file
def save_contacts(file_name, contacts):
    with open(file_name, 'w') as file:
        json.dump(contacts, file)

# Function to add a new contact
def add_contact(name, phone, email, contacts):
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to edit a contact
def edit_contact(name, new_phone, new_email, contacts):
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = new_phone
            contact['email'] = new_email
            print("Contact updated successfully.")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact(name, contacts):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

# Main function
def main():
    file_name = "contacts.json"
    contacts = load_contacts(file_name)

    while True:
        print("\nSimple Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email, contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            name = input("Enter name of contact to edit: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            edit_contact(name, new_phone, new_email, contacts)
        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            delete_contact(name, contacts)
        elif choice == '5':
            save_contacts(file_name, contacts)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
