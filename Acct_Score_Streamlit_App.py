import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Define numerical and categorical attributes
num_attributes = ['company_size', 'revenue']
cat_attributes = ['geo']
attributes = num_attributes + cat_attributes

# Create dictionaries to store entries for targets and weights
targets = {}
weights = {}

# Add input fields for targets and weights dynamically
for attribute in attributes:
    if attribute in num_attributes:
        targets[attribute] = st.number_input(f'{attribute} Target:', value=0.0)
    elif attribute in cat_attributes:
        targets[attribute] = st.text_input(f'{attribute} Preferred Category:', value='')
    
    weights[attribute] = st.number_input(f'{attribute} Weight:', value=0.0)

# Function to select CSV file
file_path = st.file_uploader('Select CSV File', type=['csv'])

# Function to handle user input and calculate scores
def handle_input():
    if file_path is None:
        st.error('Please select a CSV file.')
        return
    try:
        # Read account data
        df = pd.read_csv(file_path)
        
        # Check if CSV file contains all attributes
        if not all(attribute in df.columns for attribute in attributes):
            st.error('CSV file must contain columns for all attributes.')
            return
        
        # Check if attribute columns contain appropriate data
        if not all(pd.api.types.is_numeric_dtype(df[attribute]) for attribute in num_attributes):
            st.error('Numerical attribute columns must contain numeric data.')
            return
        if not all(pd.api.types.is_string_dtype(df[attribute]) for attribute in cat_attributes):
            st.error('Categorical attribute columns must contain string data.')
            return
        
        # Normalize numerical account data
        scaler = StandardScaler()
        df_normalized = pd.DataFrame(scaler.fit_transform(df[num_attributes]), columns=num_attributes)
        
        # Calculate fit scores
        df['fit_score'] = df_normalized.apply(lambda row: sum(weights[attribute] * abs(row[attribute] - targets[attribute]) for attribute in num_attributes), axis=1)
        df['fit_score'] += df[cat_attributes].apply(lambda row: sum(weights[attribute] * (row[attribute] == targets[attribute]) for attribute in cat_attributes), axis=1)

        # Normalize fit scores to a 100-point scale and convert to integers
        max_score = df['fit_score'].max()
        if max_score != 0:
            df['normalized_fit_score'] = (df['fit_score'] / max_score * 100).astype(int)
        else:
            st.info('All fit scores are zero, so normalization is not performed.')
        
        # Add a column for the rank of the unnormalized fit score
        df['fit_score_rank'] = df['fit_score'].rank(ascending=False)

        # Display results
        st.dataframe(df)
    except Exception as e:
        st.error(f'An error occurred: {str(e)}')

# Add submit button
if st.button('Calculate Scores'):
    handle_input()