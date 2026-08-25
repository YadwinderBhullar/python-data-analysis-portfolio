# Employee Salary Analyzer

## 📌 Project Overview

**Employee Salary Analyzer** is a small Python project created to practice **list comprehensions and dictionary comprehensions**.

The project uses employee salary data stored in a dictionary and performs several operations, including filtering employees by salary, calculating salary increases, and generating a formatted report.

The main goal is to understand how comprehensions can make Python code shorter and cleaner while still being readable.

---

## 🎯 Learning Objectives

This project practices:

* Dictionaries
* `.items()`
* Functions
* Function parameters
* Return values
* List comprehensions
* Dictionary comprehensions
* Filtering with `if`
* Mathematical calculations
* `round()`
* `zip()`
* `for` loops
* F-string formatting
* Combining multiple functions
* Creating a final report

---

## 📊 Employee Data

The project uses the following employee salary data:

```python
employees = {
    "John": 5000,
    "Sarah": 7000,
    "Mike": 4000,
    "David": 8000,
    "Lisa": 6500
}
```

The dictionary structure is:

```text
Employee Name → Salary
```

Example:

```text
John → $5,000
Sarah → $7,000
```

---

## 🧩 Functions

### 1. `get_employee_names()`

Uses a **list comprehension** to create a list containing all employee names.

```python
[name for name, salary in employees.items()]
```

---

### 2. `get_employee_salaries()`

Uses a **list comprehension** to create a list containing all employee salaries.

```python
[salary for name, salary in employees.items()]
```

---

### 3. `get_high_salary_employees()`

Uses a **dictionary comprehension** to find employees earning **$6,000 or more**.

```python
{
    name: salary
    for name, salary in employees.items()
    if salary >= 6000
}
```

---

### 4. `calculate_salary_increase()`

Calculates a **10% salary increase** for every employee.

```python
{
    name: round(salary * 1.10, 2)
    for name, salary in employees.items()
}
```

For example:

```text
$5,000 × 1.10 = $5,500
```

---

### 5. `get_low_salary_employees()`

Uses a dictionary comprehension to find employees earning **less than $6,000**.

```python
{
    name: salary
    for name, salary in employees.items()
    if salary < 6000
}
```

---

### 6. `create_salary_report()`

Calls the other functions and combines their results into one dictionary.

Conceptually:

```text
Employee Data
      ↓
Individual Functions
      ↓
Results
      ↓
Report Dictionary
```

---

### 7. `print_salary_report()`

Displays the final results in a formatted report.

This function uses:

* `for` loops
* `.items()`
* `zip()`
* f-string formatting
* number formatting

---

## 🧠 List Comprehension

A list comprehension provides a compact way to create a list.

### Normal loop

```python
employee_names = []

for name, salary in employees.items():
    employee_names.append(name)
```

### List comprehension

```python
employee_names = [
    name
    for name, salary in employees.items()
]
```

Both produce:

```text
['John', 'Sarah', 'Mike', 'David', 'Lisa']
```

---

## 🧠 Dictionary Comprehension

A dictionary comprehension creates a new dictionary from existing data.

Example:

```python
high_salary = {
    name: salary
    for name, salary in employees.items()
    if salary >= 6000
}
```

Result:

```text
{
    'Sarah': 7000,
    'David': 8000,
    'Lisa': 6500
}
```

---

## 🧠 Filtering with Comprehensions

The `if` condition allows us to filter data.

```python
{
    name: salary
    for name, salary in employees.items()
    if salary < 6000
}
```

This means:

```text
Loop through employees
        ↓
Check salary
        ↓
Is salary < 6000?
        ↓
Yes → keep employee
No  → ignore employee
```

---

## 🧠 Using `zip()`

The project also demonstrates `zip()`.

`zip()` combines corresponding values from multiple collections.

Example:

```python
names = ["John", "Sarah"]
salaries = [5000, 7000]

for name, salary in zip(names, salaries):
    print(name, salary)
```

Output:

```text
John 5000
Sarah 7000
```

In this project, `zip()` was used to combine the employee names and salary lists when displaying the report.

---

## 💰 Salary Calculation

A 10% salary increase is calculated using:

```python
salary * 1.10
```

Example:

```text
Original salary: $5,000
10% increase:      $500
New salary:       $5,500
```

The result is rounded using:

```python
round(salary * 1.10, 2)
```

---

## 🔄 Program Flow

```text
Employee Dictionary
        ↓
get_employee_names()
        ↓
get_employee_salaries()
        ↓
get_high_salary_employees()
        ↓
calculate_salary_increase()
        ↓
get_low_salary_employees()
        ↓
create_salary_report()
        ↓
print_salary_report()
        ↓
Final Report
```

---

## 📋 Example Output

```text
==================================================
          EMPLOYEE SALARY REPORT
==================================================

EMPLOYEE NAMES
--------------------------------------------------
John
Sarah
Mike
David
Lisa

EMPLOYEE SALARIES
--------------------------------------------------
John            $5,000.00
Sarah           $7,000.00
Mike            $4,000.00
David           $8,000.00
Lisa            $6,500.00

HIGH-SALARY EMPLOYEES
--------------------------------------------------
Sarah           $7,000.00
David           $8,000.00
Lisa            $6,500.00

10% SALARY INCREASE
--------------------------------------------------
John            $5,500.00
Sarah           $7,700.00
Mike            $4,400.00
David           $8,800.00
Lisa            $7,150.00

LOW-SALARY EMPLOYEES
--------------------------------------------------
John            $5,000.00
Mike            $4,000.00

==================================================
             END OF REPORT
==================================================
```

---

## 🧠 Key Lessons

The most important concepts learned in this project are:

### List comprehension

```python
[item for item in collection]
```

### List comprehension with filtering

```python
[item for item in collection if condition]
```

### Dictionary comprehension

```python
{key: value for item in collection}
```

### Dictionary comprehension with filtering

```python
{
    key: value
    for item in collection
    if condition
}
```

### Function reuse

Small functions can be combined to create a larger program.

---

## 🛠️ Technologies

* Python 3
* Visual Studio Code
* Git
* GitHub

---

## 📚 Skills Practiced

By completing this project, I practiced:

* Python dictionaries
* List comprehensions
* Dictionary comprehensions
* Filtering data
* Loops
* Functions
* Return values
* Mathematical calculations
* Data formatting
* `zip()`
* Building reusable Python programs
* Creating structured reports

---

## 🚀 Next Step

After completing this project, the next goal is to continue learning the remaining Python concepts and build a small project for each major concept.

The longer-term learning path is:

```text
Python Fundamentals
        ↓
Python Intermediate
        ↓
Python Projects
        ↓
Pandas
        ↓
SQL
        ↓
Data Analysis
```
git 