# 1st Step is to import the required modules
import os
import csv
# Getting the CVS data file 
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    
    # Read each row of data after the header and put in the list
    data = []
    
    for row in csvreader:
        data.append(row)
   
    print("Financial Analysis")
    print("----------------------------")
#   * The total number of months included in the dataset using len function
    print(f'Total Months: {len(data)}')
    
#   * The net total amount of "Profit/Losses" over the entire period. 
#   Adding all the amount from my data list
    total_amount = 0
    for i in data: 
        total_amount = total_amount+int(i[1])
    print(f'Total: ${total_amount}')
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#   Storing the difference in profit/loss between 2 consecutive months in a list.   
    change_list=[]
    for i in range (0,len(data)-1):
        change=int(data[i+1][1])-int(data[i][1])
        change_list.append(change)
    average=sum(change_list)/len(change_list)
    print(f'Average  Change: ${round(average,2)}')
#   * The greatest increase in profits (date and amount) over the entire period
#   Finding the index of the maximum change from the list and getting the corresponding month. 
    greatest_increase_month = data[change_list.index(max(change_list))+1][0]
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${max(change_list)})')

#   * The greatest decrease in losses (date and amount) over the entire period
#   Finding the index of the minimum change from the list and getting the corresponding month.    
    greatest_decrease_month = data[change_list.index(min(change_list))+1][0]
    print(f'Greatest decrease in Profits: {greatest_decrease_month} (${min(change_list)})')
#   Getting the output file to store our analysis. 
output_path= os.path.join("PyBank","analysis","Final_Analysis.txt")
with open(output_path,"w") as writer:
   
    writer.write("Financial Analysis\n")
    writer.write("----------------------------\n")
    writer.write(f'Total Months: {len(data)}\n')
    writer.write(f'Total: ${total_amount}\n')
    writer.write(f'Average  Change: ${round(average,2)}\n')
    writer.write(f'Greatest Increase in Profits: {greatest_increase_month} (${max(change_list)})\n')
    writer.write(f'Greatest decrease in Profits: {greatest_decrease_month} (${min(change_list)})\n')