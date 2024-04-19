# Acct_Score
Score accounts against custom attributes (ie. company size, industry)

**Updated: 2024.04.19**
**Project Name: Acct_Score**

**Project and Work Product Description:**

Acct_Score is a tailored solution designed to help businesses efficiently identify and prioritize potential customers that best match their Ideal Customer Profile (ICP). By enabling users to input custom attributes and their corresponding weights, the system calculates "best-fit" scores for prospective accounts. This process not only enhances the effectiveness of sales and marketing strategies but also optimizes resource allocation, leading to increased customer conversion rates. As a standalone, lightweight Python application built with Streamlit, Acct_Score reduces reliance on other complex sales and marketing tools and offers customizable scoring criteria to suit diverse market needs and business objectives.

**Description of Solution:**

Software functions for solving problem(s) step by step: Python script that will be able to intake custom ideal customer profile attributes like company size, geo, revenue, industry, etc via a GUI. The user can modify inputs for weighing attributes. Input csv file of account data to score the fit of them against the ideal customer profile attributes, output csv with scores.

	- Intake of Custom Attributes: Users can enter attributes such as company size, geography, revenue, and industry via a graphical user interface.
	- Weight Modification: Users have the flexibility to adjust the weights of different attributes based on their significance.
	- Data Processing: The application processes input CSV files containing account data and computes scores based on the predefined attributes and weights.
  	- Data Cleaning and Normalization: Step to clean data includes removing dollar symbols, converting the column to float, and filling any missing values with the mean of the column and convert range values to their midpoints.
	- Output Generation: Outputs a CSV file with accounts scored against the ideal customer profiles.
  
• MVP 1.0 Features: Basic attribute input, weight adjustments, score calculation, and CSV output.
• Future Releases (V1.x and beyond): 
 	- Improve scoring model accuracy (AI and explore packages)
   	- Improve automatic reading of CSV and auto-populating input fields
 	- Plans include adding more interactive features for data visualization, real-time data processing, and integration with CRM systems.
 • Additional requirements, Graphical User Interfaces (GUI), usability, etc. for later versions
     	- Enhanced GUI features for more intuitive user interaction, UI features like sliding scale adjustments
 	- Advanced data validation and error handling to ensure robust application performance.
    
**Solution Design (high-level):**

Acct_Score is designed as a modular, lightweight application, utilizing a client-server architecture where the front-end user interface is powered by Streamlit, and the back-end processing is handled through Python scripts. Here’s how each component contributes to the overall functionality:

	**Front-End (Streamlit Interface):** Provides a user-friendly graphical interface where users can input target values and weights for various customer attributes, upload CSV files 	containing potential customer data, and view processed scores. This interface is designed to be intuitive and accessible, allowing users to easily interact with the application 	without needing in-depth technical knowledge.
	**Back-End (Python Scripts):**
	**Data Handling:** Utilizes the pandas library to manipulate and process data. This includes reading data from CSV files, cleaning and normalizing data, and calculating fit scores 	based on user-defined criteria.
	**Data Normalization:** Employs scikit-learn for scaling numerical data to ensure that attribute weights are applied uniformly, enhancing the reliability of scoring results.
	**Calculation Engine:** Python functions are used to compute the fit scores by applying the weights to the differences between target values and actual values from the data set.
	**Integration Points:** Currently, data is input through CSV files, but future enhancements could include API integrations with CRM systems to fetch data dynamically.

**Data Flow**
The application’s data flow can be summarized in the following steps:

	**Data Input:** Users upload a CSV file via the Streamlit interface. The CSV should include data on potential customers with attributes like company size, revenue, geography, and 	industry.
	**Data Cleaning:** Upon CSV upload, the data undergoes cleaning which involves removing unnecessary formatting (e.g., dollar signs from revenue data), filling missing values, and 	converting ranges to midpoints for more uniform data.
	**Normalization:** Numerical data such as revenue and company size are normalized using standard scaling methods to ensure that they are appropriately weighted in the scoring 		process.
	**Scoring Calculation:** The application calculates scores for each entry based on the differences between the data attributes and the user-defined targets, multiplied by the 		respective weights for those attributes.
	**Output Generation:** Scores are then displayed within the Streamlit interface and can be exported to a CSV file, providing a ranked list of potential customers according to their 	fit with the user-defined ideal customer profile.

**Solution Code Description (low-level design):**

This section provides an in-depth look at the code structure, explaining the purpose and functionality of each component of the application.
 
    • Software packages (Python packages, etc.)
	- Streamlit: For building the interactive web app.
	- Pandas: Used for data manipulation and analysis.
	- Scikit-learn: For data normalization.
	- Python-dotenv: For managing environment variables (if needed).

	• Complete code: https://github.com/marketerscode/Acct_Score/

    • Key Functions
	**convert_range_to_midpoint(value)**
	- Purpose: Converts a range in string format to a numerical midpoint, or a single number string to a float.
		Input: A string that represents a numerical range (e.g., "10-20") or a single numeric value (e.g., "15").
		Output: A float that is either the midpoint of the range or the converted numeric value.
		Usage: This function is applied to data columns where range values need to be standardized to single midpoint values for consistent scoring.
	**handle_input()**
	- Purpose: Manages the overall data processing workflow from file upload to data scoring and output display.
		Process: Validates file upload and checks for necessary columns. Cleans and preprocesses the data, including removing currency symbols, filling missing values, and 			normalizing numerical attributes. Calculates fit scores based on the defined weights and target values. Outputs the results in the Streamlit interface and saves the scored 		data to a CSV file.
	**Error Handling:** Includes comprehensive error catching to inform the user of any issues during the process, such as missing data or incorrect file formats.
    
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
