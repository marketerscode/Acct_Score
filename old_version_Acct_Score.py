## Python script that will be able to intake custom ideal customer profile attributes like company size, geo, revenue, etc via a GUI. 
## The user can modify inputs for weighing attributes. 
## Input csv file of account data to score the fit of them against the ideal customer profile attributes, output csv with scores.
##
# Import necessary libraries
import tkinter as tk
from tkinter import Entry, Label, Button
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create GUI
root = tk.Tk()

# Create dictionary to store entries
entries = {}

# Add input fields for attributes and weights
attributes = ['company_size', 'geo', 'revenue']
for attribute in attributes:
    Label(root, text=attribute).pack()
    entries[attribute] = Entry(root)
    entries[attribute].pack()

# Function to handle user input
def handle_input():
    # Read user input
    user_input = {attribute: float(entries[attribute].get()) for attribute in attributes}
    
    # Read account data
    df = pd.read_csv('account_data.csv')
    
    # Normalize account data
    scaler = StandardScaler()
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    # Calculate fit scores
    df_normalized['fit_score'] = df_normalized.apply(lambda row: sum(user_input[attribute] * row[attribute] for attribute in attributes), axis=1)
    
    # Display results
    df_normalized.to_csv('output.csv', index=False)

# Add submit button
submit_button = Button(root, text="Submit", command=handle_input)
submit_button.pack()

# Start GUI
root.mainloop()
