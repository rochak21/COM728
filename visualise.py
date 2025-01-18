#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from analyse import df
import pandas as pd

# Import necessary libraries and modules


# c1. Create a pie chart to show the distribution of employees based on their education levels.
def visualise_education_proportion(df):
    """
    This function generates a pie chart that illustrates how employees are distributed across different education levels.

    Input:
        df (DataFrame): The DataFrame that holds HR metrics data.

    Output:
        None
    """
    education_counts = df['Education_level'].value_counts()
    education_counts.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
    plt.title('Distribution of Employees by Education Level')
    plt.ylabel('')
    plt.show()
print('')
# c2. Create a bar chart to compare the frequency of employee training across different education fields.
def visualise_training_frequency(df):
    """
    This function generates a bar chart to compare the frequency of employee training across different education fields.

    Input:
        df (DataFrame): A DataFrame containing HR metrics data.

    Output:
        None
    """
    training_counts = df['Education_Field'].value_counts()
    training_counts.plot(kind='bar', color='skyblue')
    plt.title('Frequency of Employee Training by Education Field')
    plt.xlabel('Education Field')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.show()
print('')

# c3. Create a bar chart to display how job satisfaction scores vary across job levels for each department.
def visualise_job_satisfaction(df):
    """
    This function produces a bar chart illustrating the changes in job satisfaction scores across different job levels within each department.

    Input:
    df (DataFrame): DataFrame containing HR metrics data.

    Output:
    None
    """
    satisfaction_dp = df.groupby(['Department', 'Job_Level'])['Job_Satisfaction'].mean().unstack()
    satisfaction_dp.plot(kind='bar', width=0.5, figsize=(10,6), rot=0)
    plt.title("Job Satisfaction Across Job Levels and Departments")
    plt.xlabel('Department')
    plt.ylabel('Average Job Satisfaction')
    plt.legend(title='Job Level', bbox_to_anchor=(1.7, 1), loc='upper left')
    plt.show()
print('')

# c4. Create a histogram to visualize the distribution of employee tenure (years at the company) across different departments.
def visualise_tenure_distribution(df):
    """
    This function generates a histogram to illustrate how employee tenure is distributed across different departments.

    Input:
        df (DataFrame): DataFrame containing HR metrics data.

    Output:
        None
    """
    plt.hist(df['Years_At_Company'], color='skyblue', width=0.7)
    plt.title('Distribution of Employee Tenure by Department')
    plt.xlabel('Years at Company')
    plt.ylabel('Number of Employees')
    plt.show()
print('')

