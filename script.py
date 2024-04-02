import json

# Create a class name Employees with fields name,id,title,department
class Employee:
    def __init__(self, name, id, title, department):
        self.name = name
        self.id = id
        self.title = title
        self.department = department

    # This function is used to display details of employee
    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.id)
        print("Title:", self.title)
        print("Department:", self.department)

    # This str function return employee name and id
    def __str__(self):
        return f"{self.name} - ID: {self.id}"


# A class represents departmentin the company, with fields name and employees
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    # This function is used to add employee to department
    def add_employee(self, employee):
        self.employees.append(employee)

    # This fun used to delete emp from the department using emp_id as agrument
    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                self.employees.remove(emp)
                return True
        return False

    # This fun simply print emp of department
    def list_employees(self):
        for emp in self.employees:
            print(emp)


# Create a class Company which cantains departmens dict field, where department_name
# consider as key of dicts and employees list as values
class Company:
    def __init__(self):
        self.departments = {}

    # This method used to add departments with employees
    def add_department(self, department):
        self.departments[department.name] = department

    # This method is used to delete department in company
    def remove_department(self, department_name):
        if department_name in self.departments.keys():
            del self.departments[department_name]
            return True
        return False

    # This method is used to display departments and its employees
    def display_departments(self):
        for department_name, department in self.departments.items():
            print("Department:", department_name)
            department.list_employees()

    # This is used to assigned list of employees as a value to key of department {}
    def to_dict(self):
        data = {}
        for department_name, department in self.departments.items():
            data[department_name] = [emp.__dict__ for emp in department.employees]
        return data


# This prints a menu for the user to interact with the Employee Management System
def menu(company):
    print("\nEmployee Management System Menu:")
    print("1 to Add Employee")
    print("2 to Remove Employee")
    print("3 to Add Department")
    print("4 to Remove Department")
    print("5 to Display Departments")
    print("6 to Exit")
    # This is used to show users available department
    print("\nAvailable Departments:")
    for department_name in company.departments:
        print(department_name)


# This is used to save the updated data to file company_data.json
def save_data(company):
    with open("company_data.json", "w") as file:
        json.dump(company.to_dict(), file,indent=4)


# This is used to existing data from file company_data.json
def load_data():
    try:
        with open("company_data.json", "r") as file:
            data = json.load(file)
            company = Company()
            for department_name, employees in data.items():
                department = Department(department_name)
                for emp_data in employees:
                    employee = Employee(
                        emp_data["name"],
                        emp_data["id"],
                        emp_data["title"],
                        department_name,
                    )
                    department.add_employee(employee)
                company.add_department(department)
            return company
    except FileNotFoundError:
        return Company()


# This is Main function to interact with the Employee Management System.
def main():
    company = load_data()
    while True:
        menu(company)
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department name: ")
            if department in company.departments:
                employee = Employee(name, emp_id, title, department)
                company.departments[department].add_employee(employee)
                save_data(company)
                print("Employee added successfully.")
            else:
                print("Department does not exist.")
        elif choice == "2":
            department = input("Enter department name: ")
            if department in company.departments:
                emp_id = input("Enter employee ID: ")
                if company.departments[department].remove_employee(emp_id):
                    save_data(company)
                    print("Employee removed successfully.")
                else:
                    print("Employee not found in department.")
            else:
                print("Department does not exist.")
        elif choice == "3":
            department_name = input("Enter department name: ")
            if department_name not in company.departments:
                department = Department(department_name)
                company.add_department(department)
                save_data(company)
                print("Department added successfully.")
            else:
                print("Department already exists.")
        elif choice == "4":
            department_name = input("Enter department name: ")
            if company.remove_department(department_name):
                save_data(company)
                print("Department removed successfully.")
            else:
                print("Department not found.")
        elif choice == "5":
            company.display_departments()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# Entry point of the script
if __name__ == "__main__":
    main()
