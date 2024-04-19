import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from datetime import datetime

# Function to convert range to midpoint
def convert_range_to_midpoint(value):
    """Convert a range string to a midpoint value, or convert a single number string to float."""
    if pd.isnull(value):
        return value
    if '-' in str(value):
        lower, upper = str(value).split('-')
        return (float(lower) + float(upper)) / 2
    else:
        return float(value)

# Main app heading
st.markdown("<h1 style='text-align: center;'>Account Scoring App</h1>", unsafe_allow_html=True)
st.markdown("This application calculates fit scores for accounts based on their attributes. "
            "Define target values and weights for each attribute to score the accounts.")

# Instructions
st.markdown("""
- **Step 1:** Specify target values and weights for each attribute using sliders.
- **Step 2:** Upload a CSV file containing the account data.
- **Step 3:** View the calculated scores and download the results.
""")

st.markdown("**Notes:**")
st.markdown("The fit score for each account is calculated as the sum of the absolute differences"
            "between the account's numerical attribute values and the target values, each multiplied"
            "by the corresponding weight, plus the sum of whether the account's categorical "
            "attribute values match the preferred categories, each multiplied by the "
            "corresponding weight.")
st.markdown("The scores are normalized to a 100-point scale by dividing each score by the "
            "maximum score and then multiplying by 100. There are 3 output columns, the raw "
            "fit score [fit_score], normalized fit score [normalized_fit_score], and the "
            "ranked raw fit score [fit_score_rank].")
st.markdown("Your uploaded CSV file must contain headers matching the fields as named: "
            "'Company Size', 'Revenue', 'Geo Location', and 'Industry'. The total weight must sum to 100.")

# Define attributes
num_attributes = ['Company Size', 'Revenue']
cat_attributes = ['Geo Location', 'Industry']
attributes = num_attributes + cat_attributes

# Dictionaries for storing target values and weights
targets = {}
weights = {}

# User inputs for targets and weights using sliders
total_weight = 0
for attribute in attributes:
    if attribute in num_attributes:
        targets[attribute] = st.number_input(f'{attribute} Target:', value=0.0)
    else:
        targets[attribute] = st.text_input(f'{attribute} Preferred Category:', value='')

    weights[attribute] = st.slider(f'{attribute} Weight:', min_value=0.0, max_value=100.0, value=25.0, step=0.1)
    total_weight += weights[attribute]

# Check total weight
if total_weight != 100:
    st.error("Total weight must sum to 100. Current total: {}".format(total_weight))
else:
    st.success("Total weight is correctly distributed.")

# CSV file uploader
file_path = st.file_uploader('Select CSV File', type=['csv'])

# Function to handle user input and calculate scores
def handle_input():
    if file_path is None:
        st.warning("Please upload a CSV file.")
        return
    
    try:
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Preprocessing and validation steps
        if not set(attributes).issubset(df.columns):
            st.error('CSV file must contain columns for all attributes.')
            return
        
        df['Revenue'] = df['Revenue'].replace(r'[\$,]', '', regex=True).astype(float)
        df['Company Size'] = df['Company Size'].apply(convert_range_to_midpoint)

        # Normalize numerical account data
        scaler = StandardScaler()
        df_normalized = pd.DataFrame(scaler.fit_transform(df[num_attributes]), columns=num_attributes)
        
        # Calculate fit scores
        df['fit_score'] = df_normalized.apply(
            lambda row: sum(weights[attribute] * abs(row[attribute] - targets[attribute])
                            for attribute in num_attributes), axis=1
        )
        df['fit_score'] += df[cat_attributes].apply(
            lambda row: sum(weights[attribute] * (row[attribute] == targets[attribute])
                            for attribute in cat_attributes), axis=1
        )
        
        # Normalize and rank fit scores
        max_score = df['fit_score'].max()
        df['normalized_fit_score'] = (df['fit_score'] / max_score * 100).astype(int) if max_score else df['fit_score']
        df['fit_score_rank'] = df['fit_score'].rank(ascending=False)
        
        # Display results and save to CSV
        st.dataframe(df)
        current_date_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        df.to_csv(f'output_{current_date_time}.csv', index=False)
        st.success('Scores calculated successfully. Download the results from the output CSV file.')
        
    except Exception as e:
        st.error(f'An error occurred: {str(e)}')

# Calculate button
if st.button('Calculate Scores') and total_weight == 100:
    handle_input()
