# Project 04: Employee Management System

employees = []

# Function to Add Employee
def add_employee():
    print("\n--- Add New Employee ---")

    employee_id = input("Enter Employee ID: ")

    # Check Duplicate Employee ID
    for employee in employees:
        if employee["ID"] == employee_id:
            print("Employee ID already exists!")
            return

    employee_name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")
    monthly_salary = float(input("Enter Monthly Salary: \u20b9"))

    annual_salary = monthly_salary * 12

    employee = {
        "ID": employee_id,
        "Name": employee_name,
        "Department": department,
        "Designation": designation,
        "Monthly Salary": monthly_salary,
        "Annual Salary": annual_salary
    }

    employees.append(employee)

    print("\nEmployee added successfully!")

# Function to View All Employees
def view_employees():
    print("\n--- Employee Records ---")

    if len(employees) == 0:
        print("No employee records found.")

    else:
        for employee in employees:
            print("-" * 40)
            print("Employee ID:", employee["ID"])
            print("Name:", employee["Name"])
            print("Department:", employee["Department"])
            print("Designation:", employee["Designation"])
            print("Monthly Salary: \u20b9", employee["Monthly Salary"])
            print("Annual Salary: \u20b9", employee["Annual Salary"])

# Function to Search Employee
def search_employee():
    print("\n--- Search Employee ---")

    search_id = input("Enter Employee ID: ")

    found = False

    for employee in employees:

        if employee["ID"] == search_id:
            print("\nEmployee Found!")
            print("Employee ID:", employee["ID"])
            print("Name:", employee["Name"])
            print("Department:", employee["Department"])
            print("Designation:", employee["Designation"])
            print("Monthly Salary: \u20b9", employee["Monthly Salary"])
            print("Annual Salary: \u20b9", employee["Annual Salary"])

            found = True
            break

    if not found:
        print("Employee not found.")

# Main Program
while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        print("Thank you for using Employee Management System!")
        break

    else:
        print("Invalid choice. Please try again.")