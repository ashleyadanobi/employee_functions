import employee_functions as fx
import pandas as pd

employee = pd.read_csv('employee1.csv')

print("Hi, welcome. Select # based on function you would like to perform")
fx_number = input("\nWould you like to: (1) calculate the Nth highest salary, (2) categorize salaries,"
                  "\n (3) find a specific value for a department's salaries or (4) compare employee salary "
                  "\n to department averages: ")

if int(fx_number) > 4 or int(fx_number) <= 0:
    print("\nINVALID INPUT. Select # based on function you would like to perform")
    fx_number = input("\nWould you like to: (1) calculate the Nth highest salary, (2) categorize salaries,"
                      "\n or (3) find a specific value for a department's salaries: ")

if int(fx_number) == 1:
    N = input("\nWhat is your N value for calculating Nth highest salary : ")
    print(fx.nth_highest_salary(employee, int(N)))

if int(fx_number) == 2:
    employee = fx.categorize_salary(employee('employee1.csv'))
    print(fx.categorize_salary(pd.read_csv('employee1.csv')))

if int(fx_number) == 3:
    # print(fx.information_by_department(pd.read_csv('employee1.csv'), 'HR', 'Minimum'))
    department_name = input("\nWhich department - HR, IT, Sales, Accounting?")
    value_name = input("\nWhat do you want to calculate for this department - Minimum, Maximum, Median, Average?")
    print(fx.information_by_department(employee, department_name, value_name))

if int(fx_number) == 4:
    # print(fx.information_compared_to_department_avg(pd.read_csv('employee1.csv'), "HR", "3"))
    department_name = input("\nWhich department - HR, IT, Sales, Accounting?")
    print("Entries are:")
    print(fx.department_ids(employee, department_name))

    value_name = input("\nWhich ID?")
    print(fx.information_compared_to_department_avg(employee, department_name, value_name))
