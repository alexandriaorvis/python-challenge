# Import os module
import os

# Import CSV module
import csv

# Define CSV path
csvpath = os.path.join('/Users/alexhammer/Desktop/Classwork/Module_Challenges/python-challenge/PyBank/Resources/budget_data.csv')

#Create a file to write results into
with open("/Users/alexhammer/Desktop/Classwork/Module_Challenges/python-challenge/PyBank/analysis/budget_text.txt", "wt") as f:

# Read the CSV file
    with open(csvpath) as budget_file:
        csvreader = csv.reader(budget_file, delimiter=",")

        # Skip header 
        next(csvreader)
    
        # Make lists to hold the values in dates column, profit and loss column, and a list to record the daily change in profit
        month_list = []
        profit_loss = []
        change_list = []

        # Print document header
        print("Financial Analysis", file = f)

        print(" ", file = f)

        print("-------------------------------", file = f)

        print (" ", file = f)


        # Set row counter to 0
        row_counter = 0

        # Set total for Profit and Loss = 0
        net_total = 0 

        # Set total change at 0
        total_change = 0 

        # Loop through every row in CSV file
        for row in csvreader:

            # Add one for every row in CSV file
            row_counter += 1

       
            # Add each date to the month list for the calculation of the date of greatest increase and decrease
            month_list.append(row[0])

            # Add each value in profit and loss
            net_total += (int(row[1]))

            profit_loss.append(row[1])

        #Loop through the profit_loss list to calculate the average change
        for i in range(len(profit_loss) - 1):

            # Total change = the sum of the change between each month over the number of months recorded
            total_change += (int(profit_loss[i+1])) - (int(profit_loss[i]))

            average_change = (total_change / (len(profit_loss) - 1))
       
            # Add each daily change to list of the each daily increase or decrease in profit (change_list)
            change_list.append(int(profit_loss[i+1]) - (int(profit_loss[i])))
       
            # Calculate the maximum increase in profits
            max_increase = max(change_list)

            # Find the index for change_list at the maximum value
            increase_index = change_list.index(max_increase)

            # Match that index with the month list index to return the date at the time of greatest increase
            increase_date = month_list[increase_index +1]

            # Calculate the maximum decrease in profits
            max_decrease = min(change_list)

            # Find the index for change_list and the minimum value
            decrease_index = change_list.index(max_decrease)

            # Match the index of the minimum value to the index on month list to return the date
            decrease_date = month_list[decrease_index +1]
    
        # Print number of rows
        print("Total Months: " + str(row_counter), file = f)

        print(" ", file = f)

        # Print the profit and loss total
        print("Total: $" + str(net_total), file = f)

        print(" ", file = f)

        # Print the average change
        average_rounded = round(average_change,2)
        print("Average Change: $" + str(average_rounded), file = f)

        print(" ", file = f)

        # Print the maximum increase and decrease in profit
        print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(max_increase) + ")" , file = f)

        print(" ", file = f)

        print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(max_decrease) + ")", file = f )
