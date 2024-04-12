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
