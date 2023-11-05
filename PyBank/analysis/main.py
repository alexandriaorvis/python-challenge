# Import os module
import os

# Import CSV module
import csv

import statistics

# Define CSV path
csvpath = os.path.join('/Users/alexhammer/Desktop/Classwork/Module_Challenges/python-challenge/PyBank/Resources/budget_data.csv')

# Read the CSV file
with open(csvpath) as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")

    # Skip header 
    next(csvreader)
    
    profit_loss = []

    # Print document header
    print("Financial Analysis")
    print("-------------------------------")


    # Set row counter to 0
    row_counter = 0

    # Set total for Profit and Loss = 0
    net_total = 0 

    # Loop through every row in CSV file
    for row in csvreader:

        # Add one for every row in CSV file
        row_counter += 1
       
        # Add each value in profit and loss
        net_total += (int(row[1]))

        profit_loss.append(row[1])


    # Print number of rows
    print("Total Months: " + str(row_counter))

    # Print the profit and loss total
    print("Total: $" + str(net_total))

