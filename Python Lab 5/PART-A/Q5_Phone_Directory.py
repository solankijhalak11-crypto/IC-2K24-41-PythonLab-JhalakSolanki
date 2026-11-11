contacts = {
    "Anita": {"phones": ["9876543210"], "email": "anita@mail.com", "city": "Pune"},
    "Manoj": {"phones": ["9123456780", "9988776655"], "email": "manoj@mail.com", "city": "Delhi"},
    "Zara": {"phones": ["9000011111"], "email": "zara@mail.com", "city": "Pune"}
}


def valid_phone(number):
    return number.isdigit() and len(number) == 10


def phone_is_used(number, current_name=""):
    for name, details in contacts.items():
        if name != current_name and number in details["phones"]:
            return True
    return False


def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return

    number = input("Enter 10-digit phone number: ").strip()
    if not valid_phone(number):
        print("Phone number must contain exactly 10 digits.")
        return
    if phone_is_used(number):
        print("This number is already saved.")
        return

    email = input("Enter email: ")
    city = input("Enter city: ")
    contacts[name] = {"phones": [number], "email": email, "city": city}
    print("Contact added.")


def add_phone():
    name = input("Enter contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    number = input("Enter another phone number: ").strip()
    if not valid_phone(number):
        print("Phone number must contain exactly 10 digits.")
    elif number in contacts[name]["phones"]:
        print("This number is already saved for the contact.")
    elif phone_is_used(number):
        print("This number belongs to another contact.")
    else:
        contacts[name]["phones"].append(number)
        print("Number added.")


def update_contact():
    name = input("Enter contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    print("1. Update email")
    print("2. Update city")
    choice = input("Choose an option: ")
    if choice == "1":
        contacts[name]["email"] = input("Enter new email: ")
        print("Email updated.")
    elif choice == "2":
        contacts[name]["city"] = input("Enter new city: ")
        print("City updated.")
    else:
        print("Invalid option.")


def delete_contact():
    name = input("Enter contact name: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def search_contact():
    print("1. Search by part of a name")
    print("2. Search by phone number")
    choice = input("Choose an option: ")

    if choice == "1":
        part = input("Enter name or part of name: ").lower()
        found = False
        for name, details in contacts.items():
            if part in name.lower():
                print(name, details)
                found = True
        if not found:
            print("No matching contact found.")

    elif choice == "2":
        number = input("Enter phone number: ").strip()
        phone_names = {
            phone: name
            for name, details in contacts.items()
            for phone in details["phones"]
        }
        if number in phone_names:
            print("Number belongs to:", phone_names[number])
        else:
            print("Number not found.")
    else:
        print("Invalid option.")


def show_reports():
    city_contacts = {}
    for name, details in contacts.items():
        city = details["city"]
        if city not in city_contacts:
            city_contacts[city] = []
        city_contacts[city].append(name)

    for city in city_contacts:
        city_contacts[city].sort()

    print("\nContacts grouped by city:", city_contacts)

    multiple = {
        name: details["phones"]
        for name, details in contacts.items()
        if len(details["phones"]) > 1
    }
    print("\nContacts with multiple numbers:", multiple)

    print("\nPhone directory in alphabetical order:")
    for name in sorted(contacts):
        print(name, contacts[name])


while True:
    print("\n--- PHONE DIRECTORY ---")
    print("1. Add contact")
    print("2. Add another number")
    print("3. Update email or city")
    print("4. Delete contact")
    print("5. Search")
    print("6. Reports")
    print("7. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        add_phone()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        show_reports()
    elif choice == "7":
        print("Program closed.")
        break
    else:
        print("Invalid option.")
