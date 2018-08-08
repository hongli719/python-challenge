# Import needed libraries
import os
import csv
from decimal import Decimal

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    vote = 0
    khan = 0
    correy = 0
    li = 0
    tooley = 0

    # Add 1 to counter if row[2] matches a candidate
    for row in csvreader:
        vote = vote + 1
        if row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Correy":
            correy = correy + 1
        elif row[2] == "Li":
            li = li + 1
        elif row[2] == "O'Tooley":
            tooley = tooley + 1

    if khan > correy and khan > li and khan > tooley:
        winner = "Khan"
    elif correy > khan and correy > li and correy > tooley:
        winner = "Correy"
    elif li > correy and li > khan and li > tooley:
        winner = "Li"
    elif tooley > tooley and khan > li and tooley > khan:
        winner = "O'Tooley"

    # Print statement
    print("\nElection Results")
    print("-------------------------")
    print(f"Total Votes: {vote}")
    print("-------------------------")
    print(f"Khan: {'{:.3f}'.format(round((khan/vote)*100,3))}% ({khan})")
    print(f"Correy: {'{:.3f}'.format(round((correy/vote)*100))}% ({correy})")
    print(f"Li: {'{:.3f}'.format(round((li/vote)*100))}% ({li})")
    print(f"O'Tooley: {'{:.3f}'.format(round((tooley/vote)*100))}% ({tooley})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Write it into a txt file
file = open("Election Results.txt", "w")

file.write("Election Results\n")
file.write("-------------------------\n")
file.write(f"Total Votes: {vote}\n")
file.write("-------------------------\n")
file.write(f"Khan: {'{:.3f}'.format(round((khan/vote)*100,3))}% ({khan})\n")
file.write(f"Correy: {'{:.3f}'.format(round((correy/vote)*100))}% ({correy})\n")
file.write(f"Li: {'{:.3f}'.format(round((li/vote)*100))}% ({li})\n")
file.write(f"O'Tooley: {'{:.3f}'.format(round((tooley/vote)*100))}% ({tooley})\n")
file.write("-------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("-------------------------")

file.close()