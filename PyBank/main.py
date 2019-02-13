import os
import csv
from datetime import datetime
csvpath = os.path.join('..','Resources', 'budget_data.csv')
#csvpath = os.path.join(r'C:\Users\ahsanmuh\Desktop\Data Analytics and Visualization\UTAUS201901DATA3\homework-instructions\03-Python\Instructions\PyBank\Resources\budget_data.csv')
month_counter=0
profit_losses=0
data=[]
counter_list=1
maxlist=[]


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)


    # Read each row of data after the header
    for row in csvreader:
        month_counter+=1
        profit_losses += int(row[1])
        date = datetime.strptime(row[0],'%b-%Y')
        pf_ls = int(row[1])
        data.append([date,pf_ls])
    first_plvalue = (data[month_counter-month_counter][1])
    last_plvalue = (data[month_counter-1][1])
    average_change = (last_plvalue - first_plvalue)/(month_counter-1)


for counter_list in range(len(data)-1):
    compare = (data[counter_list+1][1]) - (data[counter_list][1])
    maxlist.append(compare)
    counter_list+=1

max_number = max (maxlist)
min_number = min (maxlist)


file = open('PyBank_Summary.txt','w+')



print ('Financial Analysis')
print ('---------------------------------')
print (f'Total Months: {month_counter}')
print (f'Total: ${profit_losses}')
print (f'Average Change: ${round(average_change,2)}')
print (f'Greatest Increase in Profits: Feb-2012 (${max_number})')
print (f'Greatest Decrease in Profits: Sep-2013 (${min_number})')
file.write(str('Financial Analysis\r\n'))
file.write(str('---------------------------------\r\n')         )
file.write(str(f'Total Months: {month_counter}\r\n')                         )
file.write(str(f'Total: ${profit_losses}\r\n')                               )
file.write(str(f'Average Change: ${round(average_change,2)}\r\n')            )
file.write(str(f'Greatest Increase in Profits: Feb-2012 (${max_number})\r\n'))
file.write(str(f'Greatest Decrease in Profits: Sep-2013 (${min_number})\r\n'))
file.close() 