#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Define a function to load HR data from a CSV file
def load_data(filename="HR_Metrics.csv"):
    """
   This function imports HR data from a specified CSV file and stores it in a pandas DataFrame.

  
    """
    df = pd.read_csv(filename)
    return df

# Load HR data into a DataFrame (assuming this code is executed first)
df = load_data()


#  Task B1: Find the top 3 job roles with the most employees, categorized by education level
def analyse_by_job_role(df):
    """
    This function finds the top 3 job roles with the highest number of employees hired, grouped by education level.

    Parameters:
        - df (pandas.DataFrame): DataFrame containing HR data.

    Prints:
        - The top 3 job roles for each education level, along with their counts.
    """
    top_three_roles = (
        df.groupby(["Education_level", "Job_Role"])
        .size()
        .reset_index(name="Count")
        .sort_values(by=["Education_level", "Count"], ascending=[True, False])
        .groupby("Education_level")
        .head(3)
    )
    print(top_three_roles)

print('')

# Task B2: Analyze the average monthly rate of employees for each education level
def analyse_by_education_level(df):
    """
    This function determines the average monthly salary of employees based on their education level.

    Parameters:
        - df (pandas.DataFrame): DataFrame containing HR data.

    Prints:
        - The average monthly salary for each education level.
    """
    avg_monthly_rates = df.groupby("Education_level")["Monthly_Rate"].mean()
    for education_level, avg_rate in avg_monthly_rates.items():
        print(f"Average monthly rate for employees with {education_level}: {avg_rate}")
print('')
# Task B3: Analyze the average employment duration for each department
def analyse_by_department(df):
    """
    This function determines the average tenure of employees in each department.

    Arguments:
        - df (pandas.DataFrame): DataFrame containing HR data.

    Prints:
        - Average tenure for each department.
    """
    department_avg_duration = df.groupby("Department")["Years_At_Company"].mean()
    for department, avg_duration in department_avg_duration.items():
        print(f"Average employment duration in {department} department: {avg_duration}")
print('')

# Task B4: Analyze the average age of employees for each education field
def analyse_by_education_field(df):
    """
    This function calculates the mean age of employees in each education field.

    Parameters:

        df (pandas.DataFrame): DataFrame containing HR data.
    Output:

        Average age for each education field.
    """
    avg_age_by_education = df.groupby("Education_Field")["Age"].mean()
    print(avg_age_by_education)



# In[ ]:




