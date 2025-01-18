#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd

line_width = 80


def welcome(message=''):
    output = f'Operation started welcome :{message}...'
    dashes = "-" * line_width
    print(f"\n{dashes}\n{output}\n")


def load_csv_file():
    """
    Function to load data from a CSV file.

    Returns:
    - dict_data: Dictionary containing data loaded from the CSV file.
    - df_data: DataFrame containing data loaded from the CSV file.
    """
    file_path = input("Enter the file path of the CSV file: ")
    try:
        # Load data into a dictionary
        dict_data = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dict_data.append(row)

        # Load data into a DataFrame
        df_data = pd.read_csv(file_path)
        return dict_data, df_data  # Return both the dictionary and DataFrame
    except Exception as e:
        print("Error loading CSV file:", e)
        return None, None  # Return None for both dictionary and DataFrame if there's an error

def get_user_choice(user_prompt, valid_choices):

    while True:
        choice = input(user_prompt).lower()
        if choice in valid_choices:
            return choice
        else:
            invalid_choice()

def invalid_choice():  # informs the user they inputted an invalid menu choice
    print("\n Invalid choice. Please enter a valid option. \n")



# In[ ]:




