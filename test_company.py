"""
File: test_company.py
This is the test program for assignment 4.
"""

from company import Employee, Customer

customer1 = Customer("Drew Smith", \
                   "285 Andover Lane, Pompano Beach, FL, 33060", \
                   "412-555-2121", \
                   760)

employees = []
employees.append(Employee("James Chen", \
                   "87 Pierce Road, Windsor, CT, 06095", \
                   "256-555-3331", \
                   907, \
                   75000)
                 )

employees.append(Employee("Brady Parker", \
                   "80 Franklin Dr., Waterbury, CT, 06705", \
                   "756-555-3828", \
                   321, \
                   90000)
                 )

print("Customers: \n")
print(customer1, "\n")

print("Employees: \n")
for employee in employees:
    print(employee, "\n")

for employee in employees:
    if (employee == employees[1]):
        print("I found the employee with badge", employee.get_badge())


