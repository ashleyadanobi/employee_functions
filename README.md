# Employee Functions
This code modifies a 3 column employee (saved as employee1.csv) table where the columns are id (int), salary (int), and department (int) and the length can be variable.

## main.py
The console asks you which of the 4 functions in employee functions you would like to perform and adds answers to further inquiries as input to those 4 functions. This could be built into an interface at a later point

## employee_functions.py
There are 4 functions in this class. They use pandas and a table with department titles to corresponding keys is defined as a global variable

### nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame
This function returns the Nth highest salary in the employee dataframe

### categorize_salary(employee: pd.DataFrame) -> pd.DataFrame
This function adds a category value for each salary in the table based on fixed values. That value is in a new column. 

This change is irrelevant to other functions currently as I continue to call the csv file, but I could change this in further commits to change to a global employee variable created in main that's called to other functions

### def information_by_department(employee:pd.DataFrame, department_name: str, fx: str) -> int
This function finds either a minimum, maximum, median, or average value within a department. The kind of value and department are user inputs.


### def information_compared_to_department_avg(employee: pd.DataFrame, department_name: str, employee_id: int) -> str
This function finds whether an individual makes more or less then a particular department's average salary. 

Currently, you can compare salary from an id a that is NOT linked to the department b that is called, but my next changes are to: add function to determine ids within a department and return -1 for id values outside the called department



