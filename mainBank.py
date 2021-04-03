import os
import csv
#set our path to find our csv file to pull our data from
pybank_csv = os.path.join("Resources", "budget_data.csv")
#renamed our variables for more precision in code
months_total_amount = 0
net_total_amount = int(0)
profit_changes =[]

#open and read csv file
with open(pybank_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    csv_header = next(csv_reader)
#dont forget to tell csv to read the headers and the next one after that!
    first_row = next(csv_reader)
    net_total_amount += int(first_row[1])
    previous_earnings = int(first_row[1])
#now to find our total amounts we will loop through our csv file
    for row in csv_reader:
        months_total_amount = months_total_amount +1
        net_total_amount = net_total_amount + int(row[1])
        #previous_earnings = float(row[1])
        earnings_change = float(row[1]) - previous_earnings
        profit_changes.append(earnings_change)
    print(f'"Earnings change: {earnings_change}')
        #earnings_change = float(row[1]) - previous_earnings
        #earnings_change_list = [previous_earnings] + [earnings_change]
        #month_change = [row[0]] + [earnings_change_list] 
#output our results as a text and declare texfile
 #make our headers and titles now for our data, and make it organized with dash marks
    print("Financial Analysis of Bank Earnings")
    print(f'-------------------------------------------')
    print(f'The Total Months: {months_total_amount}')
    print(f'The Total Amount: ${net_total_amount}')
    print(f'-------------------------------------------',) 
      
#to find the average we will set up the loop similar to our total amount one
#new comment/ i cant do this for the life of me. Im sorry


        



        


    

    
  



