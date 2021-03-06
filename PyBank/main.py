# Import needed libraries
import os
import csv
from decimal import Decimal

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header 
    months = 0
    total = 0.0
    compare_list = []
    str_list = []
    change_list = []
    

    for row in csvreader:
              
        months = months + 1
        total = total + int(row[1])
        
        # Make a list to find greatest increase and decrease
        compare_list.append(int(row[1]))
        str_list.append(row[0])
        
    for i in range(len(compare_list)-1):
        
        # Make a list of every month changes
        change = compare_list[i+1] - compare_list[i]
        change_list.append(change)

        

    print("\nFinancial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${'{:.2f}'.format(round(total))}")
    print(f"Average  Change: ${'{:.2f}'.format(round(sum(change_list)/len(compare_list)))}")
    print(f"Greatest Increase in Profits: {str_list[compare_list.index(max(compare_list))]} (${max(compare_list)})")
    print(f"Greatest Decrease in Profits: {str_list[compare_list.index(min(compare_list))]} (${min(compare_list)})")
    
# Write it into a txt file
file = open("Financial Analysis.txt", "w")

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {months}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average  Change: ${sum(change_list)/len(compare_list)}\n")
file.write(f"Greatest Increase in Profits: {str_list[compare_list.index(max(compare_list))]} (${max(compare_list)})\n")
file.write(f"Greatest Decrease in Profits: {str_list[compare_list.index(min(compare_list))]} (${min(compare_list)})\n")

file.close()
    

    
    