import pandas as pd

file1 = pd.read_csv('File1.csv')  # File with data to be copied
file2 = pd.read_csv('File2.csv')  # File where data will be inserted

file1 = file1.rename(columns={
    
    'Member ID': 'Alternate ID',
    'First Name': 'First Name',
    'Last Name': 'Last Name',
    'Address': '1st Address Line',
    'Address2': '2nd Address Line',
    'City': 'City',
    'State': 'State',
    'Zipcode': 'Zip Code',
    'Phone 1': 'Home Phone',
    'Email': 'Email',
    'DOB': 'Employee Date Of Birth',
    'Gender': 'Gender',
    'SSN': 'Employee SSN',
    'Record Type': 'Employee Or Dependent',
    'Product Created Date': 'Date Of Hire',
    'Active Date': 'Enrollment Date',
    'Relationship': 'Relationship Code',
   

})

def map_record_type(record_type):
    if record_type.lower() == 'primary':
        return 'E'
    elif record_type.lower() == 'dependent':
        return 'D'
    else:
        return record_type  # In case there are other unexpected values
        
def map_relationship_type(record_type):
    if record_type.lower() == 'Primary':
        return 'P'
    elif record_type.lower() == 'Spouse':
        return 'S'
    elif record_type.lower() == 'Child':
        return 'C'
    else:
        return record_type  


file1['Employee Or Dependent'] = file1['Employee Or Dependent'].apply(map_record_type)
file1['Relationship Code'] = file1['Relationship Code'].apply(map_relationship_type)




# Filter out any columns in file1 that do not exist in file2
file1_filtered = file1[file2.columns.intersection(file1.columns)]

# Concatenate the filtered data from file1 into file2
combined_data = pd.concat([file2, file1_filtered], ignore_index=True)

combined_data.to_csv('combined_data.csv', index=False)

print("Data combined and saved successfully!")

