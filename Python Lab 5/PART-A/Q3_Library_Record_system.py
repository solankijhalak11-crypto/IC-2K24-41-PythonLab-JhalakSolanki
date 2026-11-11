books = {
    "ISBN101": {"title": "Python Basics", "author": "Rao", "copies": 2, "issued_to": []},
    "ISBN102": {"title": "Data Structures", "author": "Iyer", "copies": 1, "issued_to": []},
    "ISBN103": {"title": "Algorithms", "author": "Rao", "copies": 1, "issued_to": []}
}


def add_book():
    isbn = input("Enter ISBN: ")
    if isbn in books:
        extra = int(input("Enter additional copies: "))
        if extra > 0:
            books[isbn]["copies"] += extra
            print("Copies updated.")
        else:
            print("Enter a positive number.")
        return

    title = input("Enter book title: ")
    author = input("Enter author: ")
    copies = int(input("Enter number of copies: "))
    if copies <= 0:
        print("Copies must be greater than zero.")
        return

    books[isbn] = {"title": title, "author": author, "copies": copies, "issued_to": []}
    print("Book added.")


def issue_book():
    isbn = input("Enter ISBN: ")
    member = input("Enter member ID: ")

    if isbn not in books:
        print("Book not found.")
        return

    book = books[isbn]
    if book["copies"] == 0:
        print("No copies are available.")
        return
    if member in book["issued_to"]:
        print("This member already has this book.")
        return

    held_count = 0
    for item in books.values():
        if member in item["issued_to"]:
            held_count += 1

    if held_count >= 2:
        print("A member can hold a maximum of two books.")
        return

    book["copies"] -= 1
    book["issued_to"].append(member)
    print("Book issued successfully.")


def return_book():
    isbn = input("Enter ISBN: ")
    member = input("Enter member ID: ")

    if isbn in books and member in books[isbn]["issued_to"]:
        books[isbn]["issued_to"].remove(member)
        books[isbn]["copies"] += 1
        print("Book returned.")
    else:
        print("No matching issued book was found.")


def search_book():
    isbn = input("Enter ISBN: ")
    if isbn in books:
        print(books[isbn])
    else:
        print("Book not found.")


def library_reports():
    author = input("Enter author name: ").strip().lower()
    author_books = {
        isbn: book["title"] for isbn, book in books.items()
        if book["author"].lower() == author
    }
    print("\nBooks by author:", author_books)

    member_books = {}
    for book in books.values():
        for member in book["issued_to"]:
            if member not in member_books:
                member_books[member] = []
            member_books[member].append(book["title"])

    more_than_one = {member: titles for member, titles in member_books.items() if len(titles) > 1}
    print("\nMembers holding multiple books:", more_than_one)

    unavailable = {isbn: book["title"] for isbn, book in books.items() if book["copies"] == 0}
    print("\nBooks with no available copies:", unavailable)

    not_issued = {
        isbn: book["title"] for isbn, book in books.items()
        if len(book["issued_to"]) == 0
    }
    print("\nBooks never issued:", not_issued)


while True:
    print("\n--- LIBRARY RECORD SYSTEM ---")
    print("1. Add book")
    print("2. Issue book")
    print("3. Return book")
    print("4. Search book")
    print("5. Reports")
    print("6. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        library_reports()
    elif choice == "6":
        print("Program closed.")
        break
    else:
        print("Invalid option.")
