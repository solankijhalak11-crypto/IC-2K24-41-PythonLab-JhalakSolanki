employees = {
    "E01": {"name": "Kiran", "department": "IT", "salary": 60000},
    "E02": {"name": "Sara", "department": "HR", "salary": 45000},
    "E03": {"name": "Dev", "department": "IT", "salary": 75000},
    "E04": {"name": "Nina", "department": "Finance", "salary": 52000},
    "E05": {"name": "Omar", "department": "HR", "salary": 48000}
}


def add_employee():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    employees[emp_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }
    print("Employee added.")


def update_salary():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        employees[emp_id]["salary"] = float(input("Enter new salary: "))
        print("Salary updated.")
    else:
        print("Employee not found.")


def delete_employee():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted.")
    else:
        print("Employee not found.")


def search_employee():
    emp_id = input("Enter employee ID: ")
    if emp_id in employees:
        print(employees[emp_id])
    else:
        print("Employee not found.")


def employee_reports():
    department_data = {}
    for employee in employees.values():
        dept = employee["department"]
        if dept not in department_data:
            department_data[dept] = {"payroll": 0, "count": 0}
        department_data[dept]["payroll"] += employee["salary"]
        department_data[dept]["count"] += 1

    print("\nDepartment payroll and employee count:")
    for dept, data in department_data.items():
        print(dept, "Payroll:", data["payroll"], "Employees:", data["count"])

    highest = {}
    for employee in employees.values():
        dept = employee["department"]
        if dept not in highest or employee["salary"] > highest[dept]["salary"]:
            highest[dept] = employee

    print("\nHighest-paid employee in each department:")
    for dept, employee in highest.items():
        print(dept, ":", employee["name"], employee["salary"])

    print("\nEmployees sorted by salary:")
    ordered = sorted(employees.items(), key=lambda item: item[1]["salary"], reverse=True)
    for emp_id, employee in ordered:
        print(emp_id, employee["name"], employee["salary"])

    raised = {
        emp_id: {
            "name": employee["name"],
            "department": employee["department"],
            "salary": employee["salary"] * 1.10
        }
        for emp_id, employee in employees.items()
        if employee["salary"] < 50000
    }
    print("\nNew records with a 10% raise for salaries below 50000:")
    print(raised)

    totals = {}
    for employee in employees.values():
        dept = employee["department"]
        if dept not in totals:
            totals[dept] = [0, 0]
        totals[dept][0] += employee["salary"]
        totals[dept][1] += 1

    if totals:
        averages = {dept: values[0] / values[1] for dept, values in totals.items()}
        best = max(averages, key=averages.get)
        print("\nDepartment with highest average salary:", best, averages[best])


while True:
    print("\n--- EMPLOYEE DATABASE ---")
    print("1. Add employee")
    print("2. Update salary")
    print("3. Delete employee")
    print("4. Search employee")
    print("5. Show reports")
    print("6. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        update_salary()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        employee_reports()
    elif choice == "6":
        print("Program closed.")
        break
    else:
        print("Invalid option.")
