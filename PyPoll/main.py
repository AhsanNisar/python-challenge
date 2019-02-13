import os
import csv
from datetime import datetime
csvpath = os.path.join('..','Resources', 'election_data.csv')
#csvpath = os.path.join(r'C:\Users\ahsanmuh\Desktop\Data Analytics and Visualization\UTAUS201901DATA3\homework-instructions\03-Python\Instructions\PyPoll\Resources\election_data.csv')
dictNames ={}
vote_counter=0
file = open('PyPoll_Summary.txt','w+')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    file.write(str('Election Results\r\n'))
    file.write(str('---------------------------------\r\n'))
    for row in csvreader:
        vote_counter+=1
        if not (row[2] in dictNames):
            dictNames[row[2]] = 1
        else:
            dictNames[row[2]] += 1 
    print (f'Total Votes: {vote_counter}\r\n')
    file.write(str(f'Total Votes: {vote_counter}\r\n'))
    file.write(str('---------------------------------\r\n'))
    
    current = 0
    winner =""
    for key in dictNames:
        line = key+":"+""+"{0:.3f}".format(dictNames[key]/vote_counter*100)+"%"+"      "+"("+str(dictNames[key])+")"
        print (line)
        file.write(str(f'{line}\r\n'))
        
        if dictNames[key]>current:
            current = dictNames[key]
            winner = key
    file.write(str('---------------------------------\r\n'))
    winner_line = "Winner is:"+" "+winner
    print (winner_line)
    file.write(str(f'{winner_line}\r\n'))
    file.write(str(f'---------------------------------\r\n'))
    file.close() 
       