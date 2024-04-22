"""
__author__ = "Anaid Rodriguez"
__file__ = "Database Enhancement"
__institution__ = "Southern New Hampshire University"
__course__ = "CS-499 Computer Science Capstone"
__assignment__ = "5-2 Milestone Four: Enhancement Three: Databases
__date__ = 04/07/2024
__version__ = "2.0"
"""

import mysql.connector

# the connection to mysql workbench
employee_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="a317499R!",
    database="employees"
)

# for simplicity the username and password will be 'username' and 'password
username = "username"
password = "password"
employee = employee_db.cursor()
departments = """ID | Department
------------------------
1  | Human Resources
2  | Customer Service
3  | Finance
4  | Public Relations"""


# the main menu that the user will be using
def menu():
    print("\nSelect what you would like to do from the menu below\n")
    print("1. Add Employee\n"
          "2. View a List of All Employee Names\n"
          "3. View the Total Number of Employees\n"
          "4. View All Employee Records\n"
          "5. Update an Employee Record\n"
          "6. Delete An Employee Record\n"
          "7. Exit\n")


# function to verify the username is correct when logging in
def check_username():
    while True:
        user_name = input("Enter your username: ")
        if user_name == username:
            return
        else:
            print("Invalid username")


# function to verify the password is correct when logging in
def check_password():
    while True:
        user_pass = input("Enter your password: ")
        if user_pass == password:
            print("Welcome!\n")
            return
        else:
            print("Invalid password")


# function that verifies the combination of username and password is correct
def login():
    check_username()
    check_password()


# function that checks if the employee id is already in use
# this helps prevent duplicate employee id's because they're the unique identifying factor for each employee
def check_id(id):
    while True:
        if search_for_employee(id):
            print("Employee ID already in use")
            return False
        else:
            return True


# function to create the employee id
def create_id():
    while True:
        try:  # exception handling to ensure only an integer is accepted as the id
            id = int(input("Create 3-digit Employee ID: "))  # the id must be 3 digits, no more-no less
            while not check_id(id):
                id = int(input("Create 3-digit Employee ID: "))
            while len(str(id)) > 3 or len(str(id)) < 3:  # verify the length of the id
                print("Please make sure the Employee ID is 3 digits long")
                id = int(input("Create 3-digit Employee ID: "))
            return id

        except ValueError:  # if anything other than an int is inputted, there will be an exception thrown
            print("Please enter a valid 3-digit Employee ID")


# function to create the employee name
def create_name():
    first_name = input("Enter employee first name: ")
    while len(first_name) > 39 or len(first_name) < 2:  # the name must be between 2 and 39 characters
        print("Please enter a valid first name")  # the loop will iterate until a valid name is inputted
        first_name = input("Enter employee first name: ")

    last_name = input("Enter employee last name: ")
    while len(last_name) > 49 or len(last_name) < 2:  # the last name must be between 2 and 49 characters
        print("Please enter a valid last name")  # the loop will iterate until a valid last name is inputted
        last_name = input("Enter employee last name: ")

    return first_name, last_name  # return the full name


# function to select the department id for the employee
def select_dep_id():
    print('*' * 25)
    print(departments)
    while True:  # loop will continue until a valid entry is inputted
        dep_id = input("Enter employee's department ID: ")

        match dep_id:  # match case will return the selected department
            case '1':
                return 1
            case '2':
                return 2
            case '3':
                return 3
            case '4':
                return 4
            case default:
                print("Please enter valid department ID\n")


# function to select the exemption classification
def select_classification():
    print("\nWhat is the employee's exemption classification?\n"
          "1 = Exempt\n"
          "2 = Non-Exempt\n")

    while True:  # loop will continue until a valid entry is entered
        classification = input("Select 1 or 2: ")

        # if, else statement will return the entry
        if classification == '1':
            return 'Exempt'
        elif classification == '2':
            return 'Non-Exempt'
        else:
            print("Please select a valid employee classification")


# function to select the work status between full time and part time
def select_status():
    print("\nWhat is the employee's work status?\n"
          "1 = Full-Time\n"
          "2 = Part-Time\n")

    while True:  # a loop will iterate until a valid entry is inputted
        status = input("Select 1 or 2: ")

        # the if, else statement will return the entry
        if status == '1':
            return 'Full-Time'
        elif status == '2':
            return 'Part-Time'
        else:
            print("Please select a valid employee status")


# function to set the employee salary
def set_salary():
    print("\nEnter employee's yearly salary in the following format xxxxx.xx")

    while True:  # loop will iterate until a valid salary is entered
        try:  # exception handling for type of input

            salary = "{:.2f}".format(float(input()))
            if len(str(salary)) > 8:  # ensure the salary stays within the allowed range
                print("Enter employee's salary ranging up to $99999.99")
            else:
                return salary  # return the salary entered

        except ValueError:  # if anything other than integers is entered, an execption will be thrown
            print("Please enter a valid salary in the format xxxxx.xx")

 # function to search for an employee in the database
def search_for_employee(id):
    employee.execute("SELECT * FROM employee WHERE Employee_ID=(%s)", (id,))
    found = 0

    for x in employee:
        found = found + 1  # if there is a match add to the count

    if found == 1:
        return True  # if there was a match, the function will return true
    else:
        return False  # if there was no match, the function will return false

    # this function will be used to ensure there are no duplicate employee id's
    # it will also be used in the update function and the delete function to search for the employee record


# CRUD FUNCTIONS #

# CREATE function
# calls on all the functions to ask for user input for the new employee record to be created
def create_employee():
    employee_id = create_id()
    full_name = create_name()
    first_name = full_name[0]
    last_name = full_name[1]
    department = select_dep_id()
    classification = select_classification()
    status = select_status()
    salary = set_salary()

    # execute the sql function to insert into the table using the values above
    employee.execute(f"INSERT INTO employee VALUES(%s, %s, %s, %s, %s, %s, %s)", (employee_id, first_name, last_name, department, classification, status, salary))
    # commit changes to the table
    employee_db.commit()


# READ function
def read_employee_list():
    employee.execute("SELECT * FROM employee")  # sql function to read all the rows in the table
    for x in employee:
        print(x)  # prints all the rows


# UPDATE function
def update_employee():
    id = int(input("Please enter Employee ID of the employee file to edit: "))  # needs the id of the employee record to be updated
    if search_for_employee(id):  # use search function. If there is a match, the update function continues
        # the options that are available to update on an employee record
        print("\n1. Employee name\n"
              "2. Employee department\n"
              "3. Employee classification\n"
              "4. Employee status\n"
              "5. Employee salary")

        while True:  # loop that will continue if no valid option is entered to update
            update = input("Select what information to edit: ")
            match update:  # match case is used for user input
                case '1':  # case 1 calls the create name function and uses the sql update function, then commits the changes
                    new_name = create_name()
                    employee.execute(f"UPDATE employee SET First_Name = (%s), Last_Name = (%s) WHERE Employee_ID = (%s)", (new_name[0], new_name[1], id))
                    employee_db.commit()
                    return
                case '2':  # case 2 calls the department id function, uses the sql update function, then commits the changes
                    new_department = select_dep_id()
                    employee.execute(f"UPDATE employee SET Department_ID = (%s) WHERE Employee_ID = (%s)", (new_department, id))
                    employee_db.commit()
                    return
                case '3':  # case 3 calls the classification function, uses the sql update function, then commits the change
                    new_classification = select_classification()
                    employee.execute(f"UPDATE employee SET Classification = (%s) WHERE Employee_ID = (%s)", (new_classification, id))
                    employee_db.commit()
                    return
                case '4':  # case 4 calls the status function, uses the sql update function, then commits the change
                    new_status = select_status()
                    employee.execute(f"UPDATE employee SET Status = (%s) WHERE Employee_ID = (%s)", (new_status, id))
                    employee_db.commit()
                    return
                case '5':  # case 5 calls the salary function, uses the sql update function, then commits the change
                    new_salary = set_salary()
                    employee.execute(f"UPDATE employee SET Salary = (%s) WHERE Employee_ID = (%s)", (new_salary, id))
                    employee_db.commit()
                    return
                case default:  # the default case lets the user know they need to input a valid option to update
                    print("Please select what information to update\n")
    else:  # if there is no match for the id entered, the employee record does not exist
        print("That Employee ID does not exist")


# DELETE function
def delete_employee():
    id = int(input("Please enter Employee ID of the employee file to delete: ")) # enter the id of the employee record to delete
    if search_for_employee(id):  # call the search function. If the id exists in the table, run the sql delete function
        employee.execute(f"DELETE FROM employee WHERE Employee_ID = (%s)", (id,))
        employee_db.commit()
        print("Employee record successfully deleted")  # let the user know the record was deleted
    else:  # if the employee id does not exist in the table, the employee record does not exist
        print("Employee ID entered matched no records")


# the main function
def main():
    login()  # call the login function. Username = 'username', password = 'password'
    while True:  # while loop to iterate until the user exits the program
        menu()
        selection = input(">> ")
        match selection:  # match case for user input
            case '1':  # case 1 creates a new employee
                create_employee()
            case '2':  # case 2 lists the employees names
                employee.execute("SELECT First_Name, Last_Name FROM employee")
                for x in employee:
                    print(x)
            case '3':  # case 3 counts and returns the total number of employess
                employee.execute("SELECT COUNT(*) FROM employee")
                for x in employee:
                    print("Total Number of Employees:", x[0])
            case '4':  # case 4 returns all the records found
                read_employee_list()
            case '5':  # case 5 updates an employee record
                update_employee()
            case '6':  # case 6 deletes an employee record
                delete_employee()
            case '7':  # case 7 exits the program and ends the loop
                print("Logging out")
                return
            case default:  # if anything other than 1-6 is entered, the user is informed to select a valid option
                print("Please select from the available menu options")


# call the main function to execute the program
if __name__ == '__main__':
    main()
