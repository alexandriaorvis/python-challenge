# Import os module
import os

# Import CSV module
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as election_file:
    csvreader = csv.reader(election_file, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Set row counter = 0
    row_counter = 0

    # Set candidate vote counts to 0
    charles_count = 0 
    diana_count = 0 
    raymon_count = 0

    # Print document header
    print("Election Results")

    print(" ")

    print("----------------------------")

    print(" ")

    # Loop through each row and add the contents to its respective list
    for row in csvreader: 

        # Add one to row_counter for every row
        row_counter += 1

        # Add one to charles count every time his name appears in row 2
        if row[2] == "Charles Casper Stockham":
            charles_count += 1 
        
        # Add one to diana count everytime her name appears in row 2
        elif row[2] == "Diana DeGette":
            diana_count += 1

        # Add one to raymon count every time his name appears in row 2
        elif row[2] == "Raymon Anthony Doane":
            raymon_count += 1

         # Make a dictionary of candidates and their counts
        count_dict = {"Charles Casper Stockham": charles_count, "Diana DeGette": diana_count, 
                  "Raymon Anthony Doane": raymon_count}
            
    # Calculate the percentage of the votes Charles received
    charles_percentage = round(((charles_count / (row_counter)) * 100 ), 3)

    # Calculate the percentage of the votes Diana received
    diana_percentage = round(((diana_count / (row_counter)) * 100 ), 3)

    # Calculate the percentage of the votes Raymond received
    raymon_percentage = round(((raymon_count / (row_counter)) * 100 ), 3) 

    # print the total number of votes cast (based on the length of the ID list)
    print(f'Total Votes: {row_counter}')

    print(" ")

    print("----------------------------")

    print(" ")

    # Print the results
    print(f"Charles Casper Stockham: {charles_percentage}% ({charles_count})")
    print(f"Diana DeGette: {diana_percentage}% ({diana_count})")
    print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_count})")

    print(" ")

    print("----------------------------")

    print(" ")

    print(f"Winner: {max(count_dict, key=count_dict.get)}")

    print(" ")

    print("----------------------------")

