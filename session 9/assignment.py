"""
Part A: Difference between Modules and Packages

Packages and modules are essential components that aid in code organization and reusability. A module is a single file containing Python code, while a package is a collection of modules organized in a directory hierarchy.

Modules enable code reuse by grouping related functionality together. For instance, the "math" module provides various mathematical functions, and the "datetime" module deals with date and time operations.

Modules can be created using simple scripts, on the other hand packages, contain multiple modules in directories and subdirectories.

Packages, on the other hand, allow for higher-level organization by containing multiple related modules. The package hierarchy follows directories and subdirectories. For instance, the "numpy" package deals with numerical computations, containing sub-modules like "numpy.random" for random number generation.

In summary, modules are individual Python files containing code, while packages are directories with multiple modules. Both contribute to Python's modularity and facilitate code management and reuse.

Module:
import math
print(math.sqrt(25))

import datetime
print(datetime.datetime.now())

Package:
import requests
r = requests.get(‘url’)
r.status_code

import numpy as np
a = np.array([[1+2j, 2+1j], [3, 4]])
b = np.array([[5, 6+6j], [7, 8+4j]])
print(a+b)
"""

#Part B: Module math_operations.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")
    

#Main File:
import math_operations

x = 10
y = 5

# Usage of math_operations functions
print("Addition:", math_operations.add(x, y))
print("Subtraction:", math_operations.subtract(x, y))
print("Multiplication:", math_operations.multiply(x, y))

try:
    print("Division:", math_operations.divide(x, y))
except ValueError as e:
    print(e)


"""
Output:
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
"""


"""
Part C: Commomnly used Package

One widely used third-party package on PyPI is "Pandas." Pandas provides high-performance, easy-to-use data structures, and data analysis tools for Python. Its primary purpose is to handle and manipulate structured data, making it a powerful library for data wrangling and analysis.

Pandas' key functionality includes:

DataFrame: A two-dimensional tabular data structure that allows efficient data manipulation, similar to a spreadsheet or SQL table.
Data cleaning: Pandas offers functions to handle missing data and duplicate values.
Data filtering and selection: It enables slicing, filtering, and querying data easily.
Aggregation: Pandas provides methods for grouping and aggregating data.
Merging and joining: Combining data from multiple sources based on common columns.
Time series analysis: Support for handling time-based data and date functionalities.

To install numpy: pip install pandas
Use:
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

In this example, we import Pandas as "pd," create a DataFrame using the dictionary "data," and display the DataFrame. Pandas is a versatile package, widely used in data science, data engineering, and other analytical applications.
"""
