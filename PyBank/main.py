# Module 3 - PyBank
# import os module to create file paths across operating systems
import os

#import module for reading csv files
import csv

# set path for file
budgetData_path = os.path.join(os.getcwd(), 'PyBank', 'Resources', 'budget_data.csv')
# option 2: C:\\Users\\cydneyhamel\\Desktop\\Python-Challenge\\PyBank\\Resources\\budget_data.csv

# create empty lists and set variables
totalMonths = []
totalProfit = []
totalChange = []
greatestIncrease = 0
greatestIncreaseMonth = ''
greatestDecrease = 0
greatestDecreaseMonth = ''
previous = []
i = 0

# improved reading using csv module (open csv file)
with open (budgetData_path) as csvfile: 

    # store contents of csv file in variable csvreader
    data = csv.reader(csvfile, delimiter=',')

    # skip the header and then iterate (loop) through values
    header = next(data)

    for row in data:

        # calculate the total number of months included in the dataset 
        totalMonths.append(row[0])

        # calculate the total profit (net total amount of "Profit/Losses" over the entire period)
        totalProfit.append(int(row[1]))

        # If not first row...
        if i != 0:
            # difference of (current row - previous row)
            change = int(row[1]) - int(previous[1])

            # calculate the change in "Profit/Losses" over the entire period, and the average of those changes
            totalChange.append(change)
        
            # calculate the greatest increase in profits (date and amount) over the entire period
            greatestIncrease = max(totalChange)
            greatestIncreaseMonth = totalMonths[totalChange.index(greatestIncrease) +1]
            # calculate the greatest decrease in profits (date and amount) over the entire period
            greatestDecrease = min(totalChange)
            greatestDecreaseMonth = totalMonths[totalChange.index(greatestDecrease) + 1]

        # set current row as previous before continuing loop
        previous = row

        # increment the index
        i += 1

# print statements
print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months: {len(totalMonths)}")
print(f"Total: ${sum(totalProfit)}")
print(f"Average Change: ${round(sum(totalChange)/len(totalChange),2)}")
print(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})")

# output file
output_path = os.path.join(os.getcwd(), 'PyBank', 'Resources', 'PyBankAnalysis.txt') 
                           
# write changes to csv using write command
with open (output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {len(totalMonths)}\n")
    file.write(f"Total: ${sum(totalProfit)}\n")
    file.write(f"Average Change: ${round(sum(totalChange)/len(totalChange),2)}\n")
    file.write(f"Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})\n")
    file.write(f"Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})\n")


