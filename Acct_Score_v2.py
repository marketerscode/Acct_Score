## In this version of the code, an input field is created for the preferred category of each categorical attribute. 
## The user can input their preferred category for 'geo' in this field. 
## The fit score for each account is calculated as the sum of the absolute differences between the account's 
## numerical attribute values and the target values, each multiplied by the corresponding weight, 
## plus the sum of whether the account's categorical attribute values match the preferred categories, 
## each multiplied by the corresponding weight. The fit scores are then saved to a CSV file.

## The scores are normalized to a 100-point scale by dividing each score by the maximum score and then multiplying by 100.




import tkinter as tk
from tkinter import Entry, Label, Button, filedialog, messagebox
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create GUI
root = tk.Tk()
root.title('Ideal Customer Profile Scorer')

# Create dictionaries to store entries for targets and weights
targets = {}
weights = {}

# Define numerical and categorical attributes
num_attributes = ['company_size', 'revenue']
cat_attributes = ['geo']
attributes = num_attributes + cat_attributes

# Add input fields for targets and weights dynamically
for attribute in attributes:
    if attribute in num_attributes:
        Label(root, text=f'{attribute} Target:').pack()
        targets[attribute] = Entry(root)
        targets[attribute].pack()
    elif attribute in cat_attributes:
        Label(root, text=f'{attribute} Preferred Category:').pack()
        targets[attribute] = Entry(root)
        targets[attribute].pack()
    
    Label(root, text=f'{attribute} Weight:').pack()
    weights[attribute] = Entry(root)
    weights[attribute].pack()

# Function to select CSV file
def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        file_label.config(text=file_path.split('/')[-1])

file_path = ''
Button(root, text='Select CSV File', command=select_file).pack()
file_label = Label(root, text='No file selected')
file_label.pack()

# Function to handle user input and calculate scores
def handle_input():
    if not file_path:
        messagebox.showerror('Error', 'Please select a CSV file.')
        return
    try:
        # Read user input for targets and weights
        user_targets = {attribute: float(targets[attribute].get()) for attribute in num_attributes}
        user_weights = {attribute: float(weights[attribute].get()) for attribute in attributes}
        
        # Check if user input is valid
        if any(weight <= 0 for weight in user_weights.values()):
            messagebox.showerror('Error', 'Weights must be positive numbers.')
            return
        
        # Read account data
        df = pd.read_csv(file_path)
        
        # Check if CSV file contains all attributes
        if not all(attribute in df.columns for attribute in attributes):
            messagebox.showerror('Error', 'CSV file must contain columns for all attributes.')
            return
        
        # Check if attribute columns contain appropriate data
        if not all(pd.api.types.is_numeric_dtype(df[attribute]) for attribute in num_attributes):
            messagebox.showerror('Error', 'Numerical attribute columns must contain numeric data.')
            return
        if not all(pd.api.types.is_string_dtype(df[attribute]) for attribute in cat_attributes):
            messagebox.showerror('Error', 'Categorical attribute columns must contain string data.')
            return
        
        # Normalize numerical account data
        scaler = StandardScaler()
        df_normalized = pd.DataFrame(scaler.fit_transform(df[num_attributes]), columns=num_attributes)
        
        # Calculate fit scores
        df['fit_score'] = df_normalized.apply(lambda row: sum(user_weights[attribute] * abs(row[attribute] - user_targets[attribute]) for attribute in num_attributes), axis=1)
        df['fit_score'] += df[cat_attributes].apply(lambda row: sum(user_weights[attribute] * (row[attribute] == targets[attribute].get()) for attribute in cat_attributes), axis=1)

        # Normalize fit scores to a 100-point scale and convert to integers
        max_score = df['fit_score'].max()
        if max_score != 0:
            df['fit_score'] = (df['fit_score'] / max_score * 100).astype(int)
        else:
            messagebox.showinfo('Notice', 'All fit scores are zero, so normalization is not performed.')

        # Display results
        output_file = 'scored_accounts.csv'
        df.to_csv(output_file, index=False)
        messagebox.showinfo('Success', f'Scores calculated and saved to {output_file}')
    except Exception as e:
        messagebox.showerror('Error', str(e))

# Add submit button
submit_button = Button(root, text="Calculate Scores", command=handle_input)
submit_button.pack()

# Start GUI
root.mainloop()