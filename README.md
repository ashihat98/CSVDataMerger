CSV Data Merger and Column Mapper
CSV Data Merger and Column Mapper is a Python-based tool developed to automate the process of merging data from two CSV files with different column structures. 
This tool was created in response to a real-world need at work, 
where I was tasked with finding an automated solution for combining data from one CSV file into another without altering the structure or format of the primary file.
Merging datasets from different sources can be time-consuming and error-prone, especially when columns do not align correctly. This project simplifies that task by intelligently mapping and merging data, ensuring the integrity of the final output while maintaining the format of the main file.

Key Features:
Column Mapping: Matches and merges columns from the secondary file into the primary file without introducing extra or unwanted columns.
Data Standardization: Automatically converts specific values (e.g., "primary" to "E" and "dependent" to "D") for consistency with the primary file’s format.
Format Preservation: Ensures that the final output keeps the structure of the primary file intact.
Efficient Data Handling: Utilizes the pandas library for fast and effective data manipulation, even with large datasets.


Reason for This Project:
At my workplace, I was asked to find a solution that could automate the merging of data from one file into another, without changing the format or introducing unnecessary columns. 
This tool was developed to solve that problem by ensuring that the final merged file is both accurate and properly formatted.

