students = {
    101: {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chemistry": 92}},
    102: {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chemistry": 64}},
    103: {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chemistry": 69}}
}


def read_marks():
    while True:
        mark = float(input("Enter marks (0-100): "))
        if 0 <= mark <= 100:
            return mark
        print("Marks must be between 0 and 100.")


def add_student():
    roll = int(input("Enter roll number: "))
    if roll in students:
        print("This roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    subject_marks = {}
    count = int(input("Enter number of subjects: "))
    for i in range(count):
        subject = input("Enter subject name: ").strip()
        if subject:
            subject_marks[subject] = read_marks()

    students[roll] = {"name": name, "marks": subject_marks}
    print("Student record added.")


def update_marks():
    roll = int(input("Enter roll number: "))
    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name: ").strip()
    students[roll]["marks"][subject] = read_marks()
    print("Marks updated.")


def delete_student():
    roll = int(input("Enter roll number: "))
    if roll in students:
        del students[roll]
        print("Record deleted.")
    else:
        print("Student not found.")


def show_student():
    roll = int(input("Enter roll number: "))
    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")


def show_reports():
    averages = {}
    for roll, info in students.items():
        marks = info["marks"]
        if marks:
            averages[roll] = sum(marks.values()) / len(marks)

    print("\nAverage marks:")
    for roll, average in averages.items():
        print(students[roll]["name"], ":", round(average, 2))

    if averages:
        topper = max(averages, key=averages.get)
        print("Class topper:", students[topper]["name"])

    subject_topper = {}
    for info in students.values():
        for subject, mark in info["marks"].items():
            if subject not in subject_topper or mark > subject_topper[subject][1]:
                subject_topper[subject] = (info["name"], mark)

    print("\nHighest scorer in each subject:")
    for subject, result in subject_topper.items():
        print(subject, ":", result[0], "-", result[1])

    print("\nStudents scoring below 40:")
    found = False
    for info in students.values():
        low_marks = {subject: mark for subject, mark in info["marks"].items() if mark < 40}
        if low_marks:
            print(info["name"], ":", low_marks)
            found = True
    if not found:
        print("None")

    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for roll, average in averages.items():
        if average >= 90:
            grades["A"].append(students[roll]["name"])
        elif average >= 75:
            grades["B"].append(students[roll]["name"])
        elif average >= 60:
            grades["C"].append(students[roll]["name"])
        elif average >= 40:
            grades["D"].append(students[roll]["name"])
        else:
            grades["F"].append(students[roll]["name"])

    print("\nGrade-wise list:")
    print(grades)


while True:
    print("\n--- STUDENT DATABASE ---")
    print("1. Add student")
    print("2. Update marks")
    print("3. Delete student")
    print("4. Search student")
    print("5. Display reports")
    print("6. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        show_student()
    elif choice == "5":
        show_reports()
    elif choice == "6":
        print("Program closed.")
        break
    else:
        print("Invalid option.")
