#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

def load_data(file_path):
    """
    This function retrieves data from a CSV file and presents it as a list of dictionaries.

    Parameters:
        file_path (str): The file path of the CSV file.
    Returns:
        list: A collection of dictionaries containing the data.
    """
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# a1. Retrieve Gender, Age, Marital Status, and Department based on Employee number
def retrieve_by_demographic_value(data):
    """
    This function obtains Gender, Age, Marital Status, and Department corresponding to an Employee number.

    Arguments:
        data (list): A list of dictionaries with employee data.
    Output:
        tuple: Gender, Age, Marital Status, and Department. If the employee number isn't found, it returns None.
    """
    emp_number = input("Enter the employee number: ")
    print(" ")
    for row in data:
        if row['Employee_Number'] == emp_number:
            return row['Gender'], row['Age'], row['Marital_Status'], row['Department']
    return None
# a2. Retrieve Department, Education level, Total Working Years, and Standard Hours based on Job Role
def retrieve_by_job_role(data):
    """
    This function retrieves Department, Education level, Total Working Years, and Standard Hours based on Job Role.

    Args:
        data (list): A list of dictionaries containing employee data.

    Returns:
        tuple: A tuple containing Department, Education level, Total Working Years, and Standard Hours.
               Returns None if the job role is not found.
    """
    job_role = input("Enter the job role: ")
    print(" ")
    for row in data:
        if row['Job_Role'] == job_role:
            return row['Department'], row['Education_level'], row['Total_Working_Years'], row['Standard_Hours']
    return None

# a3. Retrieve Employee Number, Job Role, Marital Status, and Hourly Rate of employees whose Standard Hours are less than 60 based on department
def retrieve_by_working_hours(data):
    """
   This function gets Employee Number, Job Role, Marital Status, and Hourly Rate for employees who work less than 60 hours based on department.

    Input:
        data (list): List of dictionaries with employee data.
    Output:
        tuple: Employee Number, Job Role, Marital Status, and Hourly Rate. Returns None if no matching employees are found.
    """
    department = input("Enter the department: ")
    print(" ")
    for row in data:
        if row['Department'] == department and int(row['Standard_Hours']) < 60:
            return row['Employee_Number'], row['Job_Role'], row['Marital_Status'], row['Hourly_Rate']
    return None

# a4. Retrieve Business Travel, Department, Gender, and Education Field based on Education Level
def retrieve_job_role_info(data):
    """
    This function gets Business Travel, Department, Gender, and Education Field based on Education Level.

    Input:
        data (list): List of dictionaries with employee data.
    Output:
        tuple: Business Travel, Department, Gender, and Education Field. If the Education level isn't found, it returns None.
    """
    education_level = input("Enter the Education level: ")
    print(" ")
    for row in data:
        if row['Education_level'] == education_level:
            return row['Business_Travel'], row['Department'], row['Gender'], row['Education_Field']
    return None



# In[ ]:




