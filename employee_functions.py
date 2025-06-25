import pandas as pd

departments = pd.DataFrame({'id': [1, 2, 3, 4], 'department': ['HR', 'IT', 'Sales', 'Accounting']})


# Write a solution to find the nth highest distinct salary from the Employee table.
# If there are less than n distinct salaries, return null.
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # output always requires getNthHighestSalary(N) as column name
    col_name = "getNthHighestSalary(" + str(N) + ")"

    employee_unique = employee.drop_duplicates(subset=['salary'])

    # edge cases - invalid input
    if N > len(employee) or N <= 0 or N > len(employee_unique):
        data = {col_name: [None]}
        return pd.DataFrame(data)

    # ordering input for consistency and easy reference
    employee_sorted_salary = employee.sort_values(by='salary', ascending=False, ignore_index=True)
    employee_sorted_salary = employee_sorted_salary.drop_duplicates(subset=['salary'])

    # debugging prints
    # print("\nSorted by Salary (Descending):\n", employee_sorted_salary)
    # print(employee_sorted_salary.iloc[N - 1,1])

    # locating Nth highest salary, subtracting 1 from N because of indexing
    data = {col_name: [employee_sorted_salary.iloc[N - 1, 1]]}
    return pd.DataFrame(data)


def categorize_salary(employee: pd.DataFrame) -> pd.DataFrame:

    # labeling function for salary category
    def salary_label(s: int) -> str:
        # abnormal input
        if s < 0 or None or not type(int):
            return "N/A"
        if 34000 > s > 0:
            return "low"
        if 67000 > s > 34000:
            return "medium"
        else:
            return "high"

    employee["salary level"] = employee["salary"].apply(salary_label)

    print(employee)
    return employee


def information_by_department(employee: pd.DataFrame, department_name: str, fx: str) -> int:

    # input must match these values - not case sensitive
    if department_name.lower() == 'hr' or department_name.lower() == 'it' or department_name.lower() == 'sales' or\
       department_name.lower() == 'accounting':

        # print(departments)

        x = departments[departments['department'] == department_name]
        # print(x)
        y = int(x['id'].iloc[0])
        # print(y)

    else:
        return -1

    # Function that will be taken based on user input, not case sensitive
    fx = fx.lower()
    if fx == 'minimum':
        # print("made it")
        employee_new = employee.groupby('department')["salary"].min()
        # print(employee_new)
    elif fx == 'maximum':
        employee_new = employee.groupby('department')["salary"].max()
        # print(employee_new)
    elif fx == 'median':
        employee_new = employee.groupby('department')["salary"].median()
    elif fx == 'average':
        employee_new = employee.groupby('department')["salary"].mean()
        # print(employee_new)
    else:
        return -1

    return employee_new.loc[y]


def department_ids(employee: pd.DataFrame, department_name: str) -> pd.DataFrame:
    # finds department in department table
    if departments['department'].isin([department_name]).any():
        x = departments[departments['department'] == department_name]
        # print(x)

        # this id column is the DEPARTMENT #
        y = int(x['id'].iloc[0])
        # print(y)
        print(employee[employee['department'] == y])
        return employee[employee['department'] == y]
    else:
        return pd.DataFrame()


def information_compared_to_department_avg(employee: pd.DataFrame, department_name: str, employee_id: str) -> str:

    # determine ids and related values that match user input
    department_ids_df = department_ids(employee, department_name)

    # user input for department was wrong
    if department_ids_df.empty:
        return "Department is not valid"

    # checking if user input is in table and overriding old table
    department_ids_df = department_ids_df[department_ids_df['id'] == int(employee_id)]
    #print(department_ids_df)

    # user input for id was wrong
    if department_ids_df.empty:
        return "Employee is not in specified department"

    # print(department_ids_df['id'])

    # calculating department average for user input
    dept_avg_salary = information_by_department(employee, department_name, "average")
    # print(dept_avg_salary)

    # grabbing salary of user input (could be deleted)
    x = employee[employee['id'] == int(employee_id)]

    # print("Row that was called - ")
    # print(x)

    # same here
    x_salary = int(x['salary'].iloc[0])
    # print("Salary Is - ")
    # print(x_salary)

    # comparing salary of input id employee to department average
    if 0 < x_salary < dept_avg_salary:
        return str(x_salary) + " is lower than the average salary of " + str(dept_avg_salary)
    elif x_salary == dept_avg_salary:
        return str(x_salary) + " is the same as the average salary of " + str(dept_avg_salary)
    elif x_salary > dept_avg_salary:
        x_salary = str(x_salary)
        return str(x_salary) + " is higher than the average salary of " + str(dept_avg_salary)
    else:
        return "this is not a valid salary"
