# Acct_Score
Score accounts against custom attributes (ie. company size, industry)

**Updated: 2024.04.11**
**Project Name: Acct_Score**

**Project and Work Product Description:**

Acct_Score is a tailored solution designed to help businesses efficiently identify and prioritize potential customers that best match their Ideal Customer Profile (ICP). By enabling users to input custom attributes and their corresponding weights, the system calculates "best-fit" scores for prospective accounts. This process not only enhances the effectiveness of sales and marketing strategies but also optimizes resource allocation, leading to increased customer conversion rates. As a standalone, lightweight Python application built with Streamlit, Acct_Score reduces reliance on other complex sales and marketing tools and offers customizable scoring criteria to suit diverse market needs and business objectives.
	
	• AS-IS Workflow: [Insert diagram here] - This diagram will illustrate the current method businesses use to evaluate potential customers without Acct_Score. [TBD]
	• TO-BE Workflow: [Insert diagram here] - This diagram will demonstrate how Acct_Score streamlines and enhances the customer evaluation process. [TBD]


**Description of Solution:**

Software functions for solving problem(s) step by step: Python script that will be able to intake custom ideal customer profile attributes like company size, geo, revenue, industry, etc via a GUI. The user can modify inputs for weighing attributes. Input csv file of account data to score the fit of them against the ideal customer profile attributes, output csv with scores.

		- Intake of Custom Attributes: Users can enter attributes such as company size, geography, revenue, and industry via a graphical user interface.
		- Weight Modification: Users have the flexibility to adjust the weights of different attributes based on their significance.
		- Data Processing: The application processes input CSV files containing account data and computes scores based on the predefined attributes and weights.
		- Output Generation: Outputs a CSV file with accounts scored against the ideal customer profiles.
 
	• Workflow diagram of future ("TO-BE") state (improved processes from your solution). [TBD]
	• MVP 1.0 Features: Basic attribute input, weight adjustments, score calculation, and CSV output.
	• Future Releases (V1.x and beyond): 
 		- Improve scoring model accuracy (AI and explore packages)
   		- Improve automatic reading of CSV and auto-populating input fields
 		- Plans include adding more interactive features for data visualization, real-time data processing, and integration with CRM systems.
    • Additional requirements, Graphical User Interfaces (GUI), usability, etc. for later versions
     		- Enhanced GUI features for more intuitive user interaction, UI features like sliding scale adjustments
 		- Advanced data validation and error handling to ensure robust application performance.
    
**Solution Design (high-level): [TBD]**

**Solution Code Description (low-level design):**

This section provides an in-depth look at the code structure, explaining the purpose and functionality of each component of the application.
 
    • Software packages (Python packages, etc.)
	- Streamlit: For building the interactive web app.
	- Pandas: Used for data manipulation and analysis.
	- Scikit-learn: For data normalization.
	- Python-dotenv: For managing environment variables (if needed).

	• Complete code: https://github.com/marketerscode/Acct_Score/

Actual Working Product Code: [TBD]
    Functions, modules, packages, documentation 
    
**Application Instructions:**
        Instructions to install, set-up, and use software:
1. Clone the repository:
	git clone [https://github.com/marketerscode/Acct_Score/]
2. Create and activate the Conda environment:
	conda env create -f environment.yml
	conda activate acct_score_env
3. Install required packages:
	pip install -r requirements.txt
4. Start the application:
	python acct_score.py
Follow the GUI prompts to upload data and input attributes and weights.

Review the output CSV for scored accounts.
            
    • Additional Important Guidelines for Product Usability (for others to use your work products:
	 - Ensure all input CSV files are formatted correctly with the necessary headers as specified.
	 - Check the compatibility of your Python version with the libraries used.


Rich's 6 D Agile Process:

    Idea8
    Define
    Design
    Develop
    Debug
    Document
    Deliver
    Deploy

Jinja2 
Jinja3 ==> Jinja 



# README for Account Scoring Streamlit App
Updated 04/19/2024
MMBOSTON Updated
Data Cleaning: Added code to clean the 'Revenue' column in the DataFrame. 
This includes removing dollar symbols, converting the column to float, and 
filling any missing values with the mean of the column.
Categorical Data Handling: Added code to convert all categorical attribute 
columns to string type. This ensures that all categorical attribute columns 
contain string data, which is required for the fit score calculation.
Range to Midpoint Conversion: Updated the convert_range_to_midpoint function 
to handle non-string inputs. This function is used to convert range values in 
the 'Company Size' column to their midpoints.
Error Handling: Improved error handling in the handle_input function. The function 
now catches exceptions that occur during the fit score calculation and displays an 
error message in the Streamlit app.
Normalization: Added code to normalize the numerical account data using the StandardScaler 
from scikit-learn. This ensures that the numerical attributes are on a similar scale before 
calculating the fit scores.

## Overview

The Account Scoring Streamlit App is a web-based application that calculates fit scores for accounts based on their attributes. The fit score is a measure of how well an account matches a set of target attribute values and weights specified by the user.

## How it Works

The application uses the Streamlit library to create an interactive user interface. The user can input target values and weights for each attribute, and the application calculates the fit score for each account.

The fit score is calculated as the sum of the absolute differences between the account's numerical attribute values and the target values, each multiplied by the corresponding weight, plus the sum of whether the account's categorical attribute values match the preferred categories, each multiplied by the corresponding weight.

The application also includes a function to convert range values to their midpoint for the 'Company Size' attribute. This function is used to handle attributes that are specified as ranges rather than single values.

## How to Use

To use the application, follow these steps:

1. Open the application in your web browser.
2. For each attribute, input the target value and weight. For numerical attributes, the target value should be a number. For categorical attributes, the target value should be one of the possible categories.
3. Click the 'Calculate Fit Scores' button to calculate the fit scores for each account.
4. The fit scores will be displayed in a table. You can sort the table by any column by clicking on the column header.

## Requirements

To run this application, you will need:

- Python 3.6 or later
- Streamlit
- Pandas
- sklearn

## Installation

To install the required libraries, you can use pip:

```bash
 install streamlit pandas sklearn
```

To run the application, use the Streamlit command:

```bash
streamlit run Acct_Score_Streamlit_App.py
```

## Future Enhancements

Future enhancements to this application could include:

- Adding more attributes
- Allowing the user to upload their own data
- Adding more sophisticated scoring algorithms
- Improving the user interface

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

#### Added today 04/19/2024:
Defined numerical and categorical attributes: You've defined two lists, num_attributes and cat_attributes, to store the names of the numerical and categorical attributes, respectively. You've also created a combined list attributes.

Created dictionaries to store entries for targets and weights: You've created two dictionaries, targets and weights, to store the target values and weights for each attribute.

Added input fields for targets and weights dynamically: You've added a loop that goes through each attribute and adds an input field for its target value and weight. If the attribute is numerical, a number input field is added for the target value. If the attribute is categorical, a text input field is added for the preferred category.

Added a function to select a CSV file: You've added a file uploader that allows the user to select a CSV file.

Added a function to handle user input and calculate scores: This function loads the selected CSV file into a pandas DataFrame, cleans the data, checks if the CSV file contains all attributes and if the attribute columns contain appropriate data, normalizes the numerical account data, calculates the fit scores, replaces any non-finite fit scores with a finite value, normalizes the fit scores to a 100-point scale and converts them to integers, adds a column for the rank of the unnormalized fit score, displays the results, and writes the DataFrame to a CSV file with the current date and time.

Added a submit button: You've added a button that calls the handle_input function when clicked.