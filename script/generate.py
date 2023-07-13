import csv
import random

# Define the fields for employees.csv
employees_fields = ['id', 'name', 'surname', 'unit']

# Define the fields for assignment.csv
assignment_fields = ['employee_id', 'competence_id', 'level', 'interest']

# Define the number of employees to generate
num_employees = 30

# Define fictitious data for each field in employees.csv
names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Olivia', 'Daniel', 'Sophia', 'Andrew', 'Emma']
surnames = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Wilson', 'Davis', 'Miller', 'Clark', 'Lee', 'Harris']
practices = ['Marketing', 'Engineering', 'Finance', 'Sales', 'Operations', 'Human Resources']

# Define the available competence IDs
competence_ids = ['1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '3.1', '3.2', '3.3', '3.4', '4.1', '4.2', '4.3', '4.4', '5.1', '5.2', '5.3', '5.4']

# Generate employee data
employees = []
assignments = []
for i in range(num_employees):
    employee_id = "EMPLOYEE_" + str(i + 1)
    name = random.choice(names)
    surname = random.choice(surnames)
    practice = random.choice(practices)
    employees.append([employee_id, name, surname, practice])
    
    # Generate multiple rows for each employee in assignment.csv
    num_assignments = random.randint(1, len(competence_ids))
    for _ in range(num_assignments):
        competence_id = random.choice(competence_ids)
        level = random.randint(1, 5)
        interest = random.choice([0,1])
        assignments.append([employee_id, competence_id, level, interest])

# Write employee data to employees.csv
employees_filename = '../data/employees.csv'
with open(employees_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(employees_fields)
    writer.writerows(employees)

print(f"CSV file '{employees_filename}' has been generated with {num_employees} fictitious employees.")

# Write assignment data to assignment.csv
assignment_filename = '../data/assignment.csv'
with open(assignment_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(assignment_fields)
    writer.writerows(assignments)

print(f"CSV file '{assignment_filename}' has been generated with random assignment data.")
