# import needed libraries
import os
import csv

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
    

    for row in csvreader:
              
        months = months + 1
        total = total + int(row[1])
        
        # Make a list to find greatest increase and decrease
        compare_list.append(int(row[1]))
        str_list.append(row[0])
        


            
        
      
      


    print("\nFinancial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Greatest Increase in Profits: {str_list[compare_list.index(max(compare_list))]} (${max(compare_list)})")
    print(f"Greatest Decrease in Profits: {str_list[compare_list.index(min(compare_list))]} (${min(compare_list)})")
    
    

    
    