import os
import csv
from datetime import datetime
csvpath = os.path.join('..','Resources', 'employee_data.csv')
#csvpath = os.path.join(r'C:\Users\ahsanmuh\Desktop\Data Analytics and Visualization\UTAUS201901DATA3\homework-instructions\03-Python\ExtraContent\Instructions\PyBoss\employee_data.csv')

us_state_abbrev = {
lnew = []
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#file = open('PyPoll_Summary.txt','w+'

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print (csv_header)
    for row in csvreader:
        new_name = row[1].replace(" ",",")
        date = row[2].split("-")
        date = date[1]+"/"+date[2]+"/"+date[0]
        new_ssn = row[3]
        new_ssn = "***-**-"+ new_ssn[7:len(new_ssn)]
        lnew.append([row[0],new_name, date, new_ssn,us_state_abbrev[row[4]]])


# Specify the file to write to
output_path = os.path.join('..','Resources', 'employee_data.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(csv_header)
    
    #Write the next rows
    csvwriter.writerows(lnew)